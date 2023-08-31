function downloadPDF() {
    window.jsPDF = window.jspdf.jsPDF;
    var docPDF = new jsPDF();
    var htmlFilename = window.location.pathname.split("/").pop();
    var elementHTML = document.querySelector("body");
    docPDF.html(elementHTML, {
        callback: function (docPDF) {
            docPDF.save(htmlFilename + ".pdf");
        },
        x: 0,
        y: 0,
        width: 190,
        windowWidth: 1100
    });
}




