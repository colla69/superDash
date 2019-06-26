
let url = window.location.protocol + "//" + window.location.host + "/api/uniRest";
let wrap = document.getElementById("wrap");
let loader = document.getElementById("loader");

window.onload = function() {
    console.log("start");
    wrap.style.display = "none";
    loader.style.display = "block";
    document.body.style.height = "-webkit-fill-available";

    let request = new XMLHttpRequest;
    request.open("get",url);
    request.onload = function () {
        let data = JSON.parse(request.responseText);
        console.log(data);
        renderHTML(data);
    };
    request.send();
    //alert("All AJAX requests completed");
};

function renderHTML(data) {
    let htmlString= "" ;
    let header = data.Promo[0];
    let vl = data.Promo[1];

    Object.keys(vl).forEach(function (key) {
        console.log(key);
        htmlString += key;
    });

    let promo = data.Promo;
    makeContainer(promo[0][0], promo[1], promo[2]);
    let rnvs = data.RNVS;
    makeContainer(rnvs[0][1], rnvs[1], rnvs[2]);
    let lds = data.LDS;
    makeContainer(lds[0][2], lds[1], lds[2]);
    let algo = data.ALGO;
    makeContainer(algo[0][3], algo[1], algo[2]);

    loader.style.display = "none";
    wrap.style.display = "grid";
    document.body.style.height = "100%";
    wrap.style.height = "100%";
}

function makeContainer( header, ub, vl ) {
    //HEADER
    let container = " <div id=\"unilink\">";
    container += "<h3>"+header["name"]+"</h3>";
    container += "<div id=\"links\" style=\"width: 100%\">";
    container += "<p><a href=\""+header["link"]+"\" target=\"_blank\">UniPortal</a></p>";
    container += "<p><a href=\""+header["homepage"]+"\" target=\"_blank\">Homepage</a></p>";
    container += "<p><a href=\""+header["uebungen"]+"\" target=\"_blank\">Übungen</a></p>";
    container += "<p><a href=\""+header["files"]+"\" target=\"_blank\">Files</a></p>";
    container += "</div>";

    container += "<div id=\"lists\">";
    //ub
    container += "<ul>";
    for (let key in ub){
        container += "<li><div><a href=\""+ub[key]+"\" target=\"_blank\">"+key+"</a></div></li><br>";
    }
    //vl
    container += "</ul>";
    container += "<ul>";
    for (let key in vl){
        container += "<li><div><a href=\""+vl[key]+"\" target=\"_blank\">"+key+"</a></div></li><br>";
    }
    container += "</ul>";
    container += "</div>";

    //wrap
    container += "</div>";
    wrap.insertAdjacentHTML("beforeend",container)
}