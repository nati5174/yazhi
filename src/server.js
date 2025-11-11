const express = require('express');
const app = express()

app.use(express.json());

const WebHooks = require("./routes/webhooks")

app.get('/', (req, res) => {
    res.json("Hello")
})

app.use('/webhook', WebHooks)

app.listen(3000, () => {
    console.log("Server is running on 3000")
})