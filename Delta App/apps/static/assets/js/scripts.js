// Exportation des tables vers Excel
function ExportToExcel(type, docname = '', fn, dl) {
    var elt = document.getElementById('table');
    var wb = XLSX.utils.table_to_book(elt, { sheet: "sheet1" });
    var today = new Date();
    var date = today.getHours() + 'H' + today.getMinutes() + 'mn__' + today.getDate() + '_' + (today.getMonth() + 1) + '_' + today.getFullYear();
    var newdocname = docname + '__' + date + '.';
    return dl ?
        XLSX.write(wb, { bookType: type, bookSST: true, type: 'base64' }) :
        XLSX.writeFile(wb, fn || (newdocname + (type || 'xlsx')));
}