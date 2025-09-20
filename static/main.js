$('#clearButton').click(function() {
    $('#busqueda').val('');
});
$('#searchBtn').click(function() {
    filterMarkers();
});
$('#busqueda').keypress(function(e) {
    if (e.which === 13) filterMarkers();
});
function filterMarkers() {
    const q = document.getElementById('busqueda').value.toLowerCase();
    window.location.href = q ? `/?q=${encodeURIComponent(q)}` : "/";
}
