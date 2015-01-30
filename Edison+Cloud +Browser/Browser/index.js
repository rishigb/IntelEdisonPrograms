/*****************************************************************************************App by RISHI GAURAV BHATNAGAR******************************************************************************************************/

// Wait for Cordova to load
/*document.addEventListener("deviceready", onDeviceReady, false);
//This part is working
// Cordova is ready
var devReady = false;
/**********************************************************************************************Functions used in the code ****************************************************************************************************/
/*function onDeviceReady() {
    //this part is also working
    });
    devReady = true;
}
*/
/**********************************************************************************************Functions used in the code ****************************************************************************************************/
var flag_ques1 = 0;
var flag_ques2 = 0;
var number = 0;
var flg = 0;
$(document).ready(function () {
    
    recievedevent("Start");
    /*
Write all your functions related to the HTML tags here
 */
 
});

function recievedevent(id) {
    $.ajax({
        //url:"http://localhost:3000",
        url: "https://lit-caverns-9397.herokuapp.com/",
        type: 'GET',
        success: recall
    })
}

function recall(data) {
    if (data == 0) { // In stock    
        if (flg == 1) {
            flg = 0;
        }
        resetAll();
        recievedevent('again');
    } else if (data == 1) { //Out Of Stock
        if (flg == 0) {
            //window.plugin.notification.local.add({ id:123, message: 'OutOfStock' });
            //navigator.notification.beep(1);
            //navigator.notification.alert('Shelf out of stock',dummy,'Alert','OK');
            //window.plugin.notification.local.cancel({ id:123});
            setTimeout(function(){stepOne();},1000);

            flg = 1;
        }
        $("#AlertList").show();
        recievedevent('again');
    } else {
        recievedevent('again');

        //resetAll();
    }
}


function dummy() {}

function stepOne() {
    $('#sec0').slideToggle();
    $('#ques2').hide();
    $('#final').hide();
    $('#sec1').show();
}

function resetAll() {
    $('#bottomRight').hide();
    $('#sec1').hide();
    $('#sec2').hide();
    $('#ques2').hide();
    $('#final').hide();
    $('#ques1').show();
    $('#sec0').show();
}