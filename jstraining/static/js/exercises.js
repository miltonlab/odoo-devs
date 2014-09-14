
(function () {

    appex = {};

    function main(){
	$("button").click(function (){
	    plusmultplus(1,2,3,4).then(function (r){
		console.log("(1 + 2) * (3 + 4) = ", r.multiplication);
	    });
	});
    }

    appex.main = main;

    function plusmultplus(a, b, c, d) {

	var plus1=$.ajax("/service_plus",{type:"POST", data: JSON.stringify({"a":a, "b":b}), 
					  dataType: "json", contentType:"application/json"});

	var plus2=$.ajax("/service_plus",{type:"POST", data: JSON.stringify({"a":c, "b":d}), 
					  dataType: "json", contentType:"application/json"});
	
	return $.when(plus1, plus2).then(function(r1, r2){
	    return $.ajax("/service_mult",{
		type:"POST", data: JSON.stringify({"a":r1[0].addition, "b":r2[0].addition}), 
		dataType: "json", contentType:"application/json"});});

    }

})();
