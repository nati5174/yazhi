const express = require('express')
const router = express.Router()

router.post("/", (req, res) => {
    console.log(req.body)

    try{
        res.status(200).json(req.body)
    }

    catch (err){
        console.log(err)
        res.status(404)
    }

});

module.exports = router;