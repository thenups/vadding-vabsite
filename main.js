var dict = {
    'saag': 1,
    'tandoori': 2,
    'masala': 3
};

function whichSite(psw) {

    var psw = prompt("Please enter your password:");

    try {
        var val = dict[psw]
        console.log(val);
    }
    catch(err) {
        while (err) {
            alert("Incorrect Password");
            return promptPass();
    }

};
