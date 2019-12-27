"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const block_1 = require("./block");
// import Datastore from 'nedb';
// const database = new Datastore('database.db');
// Class: Blockchain calculation module
class blockchain {
    // Hash Table
    constructor(capacity) {
        this.user = ['Amy', 'Belly', 'Chris'];
        this.capacity = capacity;
        this.user_data = Array(this.capacity).fill(null);
    }
    ;
    // Init Block ID : 0
    initBlock() {
        for (let bucket = 0; bucket < this.user.length; bucket++) {
            this.user_data[bucket] = new block_1.Block(0, this.user[bucket], 'SERVER', 10000, 10000, null, '00000');
        }
        ;
    }
    ;
    // Create new Block for a TRANSACTION
    addBlock(data) {
        if (data.sender == data.receiver)
            return ['Error: Sender and Receiver are the same!'];
        if (this.checkResBlock(data) == false)
            return ['Error: Invalid Value!'];
        let sender_bucket = this.user.findIndex(bucket => bucket == data.sender);
        let receiver_bucket = this.user.findIndex(bucket => bucket == data.receiver);
        if (this.user_data[sender_bucket] == null || this.user_data[receiver_bucket] == null)
            return ["Error: Bucket's user is empty!"];
        let sender_detail = this.getChainSize(this.user_data[sender_bucket]);
        let receiver_detail = this.getChainSize(this.user_data[receiver_bucket]);
        if (sender_detail[2] < data.amount)
            return [`Error: Transaction failed! (${data.sender} is not enough MONEY !)`];
        sender_detail[0].next = new block_1.Block(sender_detail[1], data.receiver, data.sender, parseInt('-' + data.amount), sender_detail[2] - data.amount, null, sender_detail[3]);
        receiver_detail[0].next = new block_1.Block(receiver_detail[1], data.sender, data.receiver, data.amount, receiver_detail[2] + data.amount, null, receiver_detail[3]);
        // database.insert(sender_detail[0].next,receiver_detail[0].next);
        let state = ['Done', sender_detail[0].next, receiver_detail[0].next, sender_bucket, receiver_bucket];
        return state;
    }
    ;
    /* Block  Pattern */
    // --> block_id / receiver / sender / amount / total / next / prev_hash
    // Loop to get the latest NODE [ID,TOTAL,PREV_HASH]
    getChainSize(current) {
        let block_count = 0;
        while (current.next != null) {
            current = current.next;
            block_count++;
        }
        ;
        return [current, block_count + 1, current.total, current.hash];
    }
    ;
    // Check data type
    checkResBlock(data) {
        console.log(typeof(data.receiver),typeof(data.sender),typeof(data.amount))
        return typeof data.receiver === 'string'
            && typeof data.sender === 'string'
            && typeof data.amount === 'number';
    }
    ;
    getBlockData() {
        let temp = this.user_data;
        return temp;
    }
    ;
}
exports.blockchain = blockchain;
// TEST DATA
// let obj = new blockchain(3);
// obj.initBlock();
// let data_set_1 = {
//     sender : 'Amy',
//     receiver : 'Belly',
//     amount: 50
// }
// let data_set_2 = {
//     sender : 'Belly',
//     receiver : 'Chris',
//     amount: 20
// }
// let y = obj.addBlock(data_set_1);
// let x = obj.addBlock(data_set_2);
// console.log(y)
// console.log(x)
// console.log(obj.user_data[1].next)
