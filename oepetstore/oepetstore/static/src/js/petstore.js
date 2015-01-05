
openerp.oepetstore = function(instance) {
    var _t = instance.web._t,
        _lt = instance.web._lt;
    var QWeb = instance.web.qweb;

    instance.oepetstore = {};

    // Testing class notations
    instance.oepetstore.MyClass = instance.web.Class.extend({
	init = function(name){
	  this.name = name;  
	},
	say_hello = function(){
	    console.log('hello man ', this.name);
	};
    });
    my_object = new instance.oepetstore.MyClass("Vicente");
    //my_object.name = "Vicente";
    my_object.say_hello();
    // Inheriting
    instance.oepetstore.MySpanishClass = instance.oepetstore.MyClass.extend({
	say_hello = function(){
	    this._super();
	    console.log('translation in spanish: hola hombre ', this.name);
	};
    });
    my_object2 = new instance.oepetstore.MySpanishClass("Viche");
    my_object2.say_hello();

    /////

    instance.oepetstore.HomePage = instance.web.Widget.extend({
        start: function() {
            console.log("pet store home page loaded");
        },
    });
    
    instance.web.client_actions.add('petstore.homepage', 'instance.oepetstore.HomePage');
}
