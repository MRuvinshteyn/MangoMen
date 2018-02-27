var lol;
function updateSearch(query) {
    $.get("/search", {"query": query}, updateResults);
}

function updateResults(results) {
    $("#results").empty();
    results = results.split(',');
    lol = results;
    results.forEach(function(r) {
        console.log(r);
        var elem = document.createElement('div');
        elem.innerHTML = r;
        $("#results").append(elem);
    });
}
