var express = require('express');
var path = require('path')
var app = express();

app.use(express.urlencoded({ extended: true }));

app.get('/', function (req, res) {
   res.sendFile(path.join(__dirname, 'index.html'));
})

app.post('/', function (req, res) {
    var password = req.body.password

    if(password == 'ocviek'){
        res.send('The password is: gFrghFdhvdu')
    }else{
        res.send('Wrong password')
    }
})

var server = app.listen(8081, function () {
   var host = server.address().address
   var port = server.address().port
   
   console.log("Example app listening at http://%s:%s", host, port)
})