$(document).ready(function() {
    console.log("ready!");

    function search() {
        $('#result').html('');

        var language = $("#ddl-languages").val();
        var search_text = $("#txt-search").val();

        console.log("language", language);
        console.log("search_text", search_text);

        var dict_file = "dictionary-eng-tr.json";
        if (language == "eng-tr") {
            dict_file = "dictionary-eng-tr.json"
        } else if (language == "tr-eng") {
            dict_file = "dictionary-tr-eng.json"
        } else if (language == "fr-eng") {
            dict_file = "dictionary-fr-eng.json"
        } else if (language == "eng-fr") {
            dict_file = "dictionary-eng-fr.json"
        }

        var expression = new RegExp(search_text, "i");

        if (search_text.length > 1) {
            $.getJSON("assets/data/" + dict_file, function(data) {
                $.each(data, function(key, value) {
                    if (expression.test(value.word)) {
                        $('#result').append('<li class="list-group-item link-class"><b>' + value.word + '</b> : ' + value.translation + '</li>');
                    }
                });
            });
        }
    }

    $.ajaxSetup({ cache: false });
    $('#txt-search').keyup(function() {
        search();
    });

    $("#btn-search").click(function() {
        search();
    });

    $("#ddl-languages").change(function() {
        $('#result').html('');
        $('#txt-search').html('');

    });
});