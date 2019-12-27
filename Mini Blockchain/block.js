"use strict";
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (Object.hasOwnProperty.call(mod, k)) result[k] = mod[k];
    result["default"] = mod;
    return result;
};
Object.defineProperty(exports, "__esModule", { value: true });
const crypto = __importStar(require("crypto"));
// Class: Use to create Node
class Block {
    // Empty Node
    constructor(block_id, receiver, sender, amount, total, next = null, prev_hash) {
        this.block_id = block_id;
        this.timestamp = new Date().getTime();
        this.receiver = receiver;
        this.sender = sender;
        this.amount = amount;
        this.total = total;
        this.prev_hash = prev_hash;
        this.hash = this.hashValue(this.block_id, this.timestamp, this.prev_hash);
        this.next = next;
    }
    ;
    // Hash
    hashValue(block_id, timestamp, prev_hash) {
        const temp = crypto.createHash('sha256');
        temp.update(block_id + timestamp + prev_hash);
        return temp.digest('hex');
    }
    ;
}
exports.Block = Block;
// TO-DO:
// DATA to import
// --> latest index
// --> previous block's total
// --> previous block's hash value
// TEST DATA:
// let obj = new Block(1,'John','SERVER',50,50,null,'asdjksjkfnkrermfdsad')
