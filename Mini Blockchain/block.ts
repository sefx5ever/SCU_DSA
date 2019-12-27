import * as crypto from 'crypto';

// Class: Use to create Node
export class Block {
    public block_id: number;
    public timestamp: number;
    public receiver: string | null;
    public sender: string | null;
    public amount:number;
    public total: number;
    public next: string | null;
    public hash: string;
    public prev_hash: string;

    // Empty Node
    constructor(block_id:number,receiver:string | null,sender:string | null,amount:number,total: number,next: string | null = null,prev_hash: string){
        this.block_id = block_id;
        this.timestamp = new Date().getTime();
        this.receiver = receiver;
        this.sender = sender;
        this.amount = amount;
        this.total = total;
        this.prev_hash = prev_hash;
        this.hash = this.hashValue(this.block_id,this.timestamp,this.prev_hash);
        this.next = next;
    };

    // Hash
    hashValue(block_id:number,timestamp:number,prev_hash:string) {
        const temp = crypto.createHash('sha256');
        temp.update(block_id+timestamp+prev_hash);
        return temp.digest('hex');
    };
}

// TO-DO:
// DATA to import
// --> latest index
// --> previous block's total
// --> previous block's hash value


// TEST DATA:
// let obj = new Block(1,'John','SERVER',50,50,null,'asdjksjkfnkrermfdsad')