const express = require("express");
const app = express();

app.get("/",function(req,res){
    res.send("hello There!");
})

app.listen(3000,function(){
    console.log("Server have started on port 3000")
})