var flag_b = 0; //To keep an accout of what has been bought and what hasn't.
var bufferList = ["salt", "sugar"]; //To keep account of all the products being added
//on instance from the server, get the value from the server and add it inside the dom.
$(document).ready(function () {
    recievedevent("Start");
    $('#NewThings').on("swiperight", 'div', function () {
        //alert("here");
        $(this).remove();
        flag_b = 1; //Bought it , remove it
    });
    $('#NewThings').on("swipeleft", 'div', function () {
        $(this).remove();
        //alert("Workin");
        flag_b = 0; //Not bought ,save it for later
        alert("Going to save it for later, Thanks!");
    });


/********************************************************************* Call from server *************************************************/

    function recievedevent(id) {
        $.ajax({
            url:"https://secure-anchorage-4352.herokuapp.com/bitval",
            
            type: 'GET',
            success: checkDuplicate
        })
    }

    function recievedevent1(id) {
        $.ajax({
            url:"https://secure-anchorage-4352.herokuapp.com/product",
            
            type: 'GET',
            success: changeProduct
        })
    }

    function checkDuplicate(data) {

        if (data == "0") {
            //call server 
            console.log("New Value");

            setTimeout(function () {
                recievedevent1("Start");
            }, 5000);

        } else {
            console.log("Repeated Value");
            setTimeout(function () {
                recievedevent("again");
            }, 5000);

        }
    }

    function changeProduct(data1) {
        if (data1 != "none") {
            //add to the DOM
            console.log(data1);
            document.getElementById("NewThings").innerHTML += " <div class=\"row\">" + "<div class=\"col-sm-4\">" + "</div><div class=\"col-sm-4 swipable\">" + "<button class=\"btn-danger\">" + data1 + "</button>" + "</div>" + "<div class=\"col-sm-4\">" + "</div></div> ";

            setTimeout(function () {
                recievedevent("Start");
            }, 5000);

        } else {
            //check for the event again. 
            setTimeout(function () {
                recievedevent("Start");
            }, 5000);
        }
    }

});