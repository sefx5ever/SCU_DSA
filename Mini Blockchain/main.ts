// Basic Setting and Library import
import express from 'express';
import socket from 'socket.io';
import { blockchain } from './blockchain';
const app = express();

// Connection condition setting
app.use(express.static('public'));
app.use(express.json({ limit : '1mb' }));

// Elastic port access
const port = process.env.PORT || 3000;
const server = app.listen(port, () => console.log(`Connect Port ${port}`));
const io = socket(server);

// Initialize blockchain in capacity = 3
let obj = new blockchain(3);
obj.initBlock();

// API: Test Connection
app.post('/api', (req:any,res:any) => {
    res.send('JIE Coin API connected successfully!').end();
});

// API: Get all Block Data
app.get('/api/getBlock', (req:any,res:any) => {
    res.send(obj.getBlockData()).end();
});

// API: New Transaction
app.post('/api/transaction', (req:any,res:any) => {
    let blockStatus = obj.addBlock(req.body);
    if ( blockStatus[0] != 'Done' ) {
        console.log(blockStatus[0]);
        res.send(blockStatus[0]).end();
    } else {
        console.log(blockStatus[0]);
        res.send(req.body).end();
        io.emit('new-transaction',{data1: [blockStatus[1],blockStatus[3]],data2: [blockStatus[2],blockStatus[4]]})
    }
});

let connectCounter = 0;
io.on('connection', (e:any) => { console.log("Conneted's User: "+ connectCounter++) });
io.on('disconnect', (e:any) => { console.log("Conneted's User: "+ connectCounter--) });