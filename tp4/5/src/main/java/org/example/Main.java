package org.example;

import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.*;
import org.apache.lucene.index.*;
import org.apache.lucene.queryparser.classic.QueryParser;
import org.apache.lucene.search.*;
import org.apache.lucene.store.*;
import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.text.PDFTextStripper;
import org.apache.poi.xwpf.usermodel.XWPFDocument;
import org.apache.poi.xwpf.usermodel.XWPFParagraph;
import org.jsoup.Jsoup;

import java.io.*;
import java.nio.file.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // Carpeta donde están los documentos a indexar
        String docsPath = "Libros";
        // Carpeta donde se guarda el índice Lucene
        String indexPath = "lucene_index";
        // Lista de extensiones de archivos que vamos a indexar
        List<String> exts = Arrays.asList(".pdf", ".docx", ".txt", ".html");

        // Abrimos (o creamos si no existe) el índice Lucene
        Directory dir = FSDirectory.open(Paths.get(indexPath));
        StandardAnalyzer analyzer = new StandardAnalyzer();
        IndexWriterConfig iwc = new IndexWriterConfig(analyzer);
        iwc.setOpenMode(IndexWriterConfig.OpenMode.CREATE_OR_APPEND); // No borra el índice, solo agrega/actualiza
        IndexWriter writer = new IndexWriter(dir, iwc);

        // Recorremos todos los archivos de la carpeta Libros
        Files.walk(Paths.get(docsPath)).filter(Files::isRegularFile).forEach(path -> {
            String ext = path.toString().toLowerCase();
            // Solo indexamos si la extensión está en la lista
            if (exts.stream().anyMatch(ext::endsWith)) {
                try {
                    // Extraemos el texto del archivo (PDF, DOCX, TXT o HTML)
                    String content = extractText(path.toFile());
                    if (content.trim().isEmpty()) return; // Si no hay texto, lo saltamos
                    // Antes de indexar, borramos cualquier documento previo con el mismo path (así no hay duplicados)
                    writer.deleteDocuments(new Term("path", path.toString()));
                    Document doc = new Document();
                    doc.add(new StringField("path", path.toString(), Field.Store.YES)); // Guardamos la ruta
                    doc.add(new TextField("content", content, Field.Store.YES)); // Guardamos el texto
                    writer.addDocument(doc);
                    System.out.println("Indexado: " + path); // Avisamos por consola
                } catch (Exception e) {
                    System.out.println("Error indexando " + path + ": " + e.getMessage());
                }
            }
        });
        writer.close();
        System.out.println("Indexación completa.");

        // Ahora viene la parte de búsqueda interactiva
        DirectoryReader reader = DirectoryReader.open(FSDirectory.open(Paths.get(indexPath)));
        IndexSearcher searcher = new IndexSearcher(reader);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            // Pedimos al usuario que escriba una consulta
            System.out.print("\nBuscar (o 'salir'): ");
            String queryStr = br.readLine();
            // Si escribe 'salir', terminamos el programa
            if (queryStr.equalsIgnoreCase("salir")) break;
            // Creamos el parser y ejecutamos la búsqueda
            QueryParser parser = new QueryParser("content", analyzer);
            Query query = parser.parse(queryStr);
            TopDocs results = searcher.search(query, 10); // Mostramos hasta 10 resultados
            System.out.println("Resultados:");
            for (ScoreDoc sd : results.scoreDocs) {
                Document d = searcher.doc(sd.doc);
                System.out.println("- " + d.get("path")); // Mostramos la ruta del archivo encontrado
            }
        }
        reader.close();
    }

    // Esta función extrae el texto de un archivo según su tipo
    public static String extractText(File file) throws Exception {
        String name = file.getName().toLowerCase();
        if (name.endsWith(".pdf")) {
            // Si es PDF, usamos PDFBox
            try (PDDocument pdf = PDDocument.load(file)) {
                return new PDFTextStripper().getText(pdf);
            }
        } else if (name.endsWith(".docx")) {
            // Si es DOCX, usamos Apache POI
            try (FileInputStream fis = new FileInputStream(file)) {
                XWPFDocument docx = new XWPFDocument(fis);
                StringBuilder sb = new StringBuilder();
                for (XWPFParagraph p : docx.getParagraphs()) {
                    sb.append(p.getText()).append("\n");
                }
                return sb.toString();
            }
        } else if (name.endsWith(".txt")) {
            // Si es TXT, leemos el archivo como texto plano
            return new String(Files.readAllBytes(file.toPath()));
        } else if (name.endsWith(".html")) {
            // Si es HTML, usamos Jsoup para limpiar las etiquetas
            String html = new String(Files.readAllBytes(file.toPath()));
            return Jsoup.parse(html).text();
        }
        return ""; // Si no es ninguno de los anteriores, devolvemos vacío
    }
} 