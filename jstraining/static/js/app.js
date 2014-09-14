
(function() {

    app = {};

    function main() {
	//debugger;
        console.log("launch application");
	var s=0
	_.each(_.range(1,1001), function(n){
	    s+=n;
	});
	console.log(s)
    };

    app.main = main;

})();
