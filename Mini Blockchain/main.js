"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
// Basic Setting and Library import
const express_1 = __importDefault(require("express"));
const socket_io_1 = __importDefault(require("socket.io"));
const blockchain_1 = require("./blockchain");
const app = express_1.default();
// Connection condition setting
app.use(express_1.default.static('public'));
app.use(express_1.default.json({ limit: '1mb' }));
// Elastic port access
const port = process.env.PORT || 3000;
const server = app.listen(port, () => console.log(`Connect Port ${port}`));
const io = socket_io_1.default(server);
// Initialize blockchain in capacity = 3
let obj = new blockchain_1.blockchain(3);
obj.initBlock();
// API: Test Connection
app.post('/api', (req, res) => {
    res.send('JIE Coin API connected successfully!').end();
});
// API: Get all Block Data
app.get('/api/getBlock', (req, res) => {
    let temp = obj.getBlockData();
    res.send(temp).end();
});
// API: New Transaction
app.post('/api/transaction', (req, res) => {
    let blockStatus = obj.addBlock(req.body);
    if (blockStatus[0] != 'Done') {
        console.log(blockStatus[0]);
        res.send(blockStatus[0]).end();
    }
    else {
        console.log(blockStatus[0]);
        res.send(req.body).end();
        io.emit('new-transaction', { data1: [blockStatus[1], blockStatus[3]], data2: [blockStatus[2], blockStatus[4]] });
        console.log(obj.user_data);
    }
});

let connectCounter = 0;
io.on('connection', (e) => { 
    console.log("Conneted's User: " + connectCounter++); 
    io.on('disconnect', (e) => { 
        console.log("Conneted's User: " + connectCounter--); 
    });
});

