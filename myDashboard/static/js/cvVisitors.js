
let url = "https://cv.colarietitosti.info/visitors";

let wrap = document.getElementById("wrap");
let loader = document.getElementById("loader");


function renderHTML(data) {
    let htmlString= "" ;


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
    container += "<p><a href=\""+header["cloudlink"]+"\" target=\"_blank\">Files</a></p>";
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