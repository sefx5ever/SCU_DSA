const socket = io.connect('http://localhost:3000');
// fetch('/api/getBlock').then( res => {
//     let temp = res.json();
//     for(let bucket = 0; bucket < 3; bucket++){
//         while ( temp != null ){
//             createBlockHTML(temp.block_id,temp.timestamp,temp.receiver,temp.sender,temp.amount,temp.total,temp.prev_hash,temp.hash,bucket+1);
//         }
//     }
// });

function sendTransaction(){
    let data_set = {
        sender : document.getElementById('sender').value,
        receiver : document.getElementById('receiver').value,
        amount : parseInt(document.getElementById('amount').value)
    };

    if (data_set.sender == data_set.receiver) {return alert('Error: Failed to SEND !!! SENDER and RECEIVER are the same person.')};
    if (typeof(data_set.amount) != "number" || data_set.amount == '') {return alert('Error: Amount only accept number type.')};

    const options = {
        method : 'POST',
        headers : {
            'Content-Type' : 'application/json'
        },
        body : JSON.stringify(data_set)
    };
    document.getElementById('amount').value = '';
    fetch('/api/transaction', options);
    //console.log(res)
};

function createBlockHTML(block_id,timestamp,receiver,sender,amount,total,prev_hash,hash,person){
    let div_block = document.createElement('div');
    let ul = document.createElement('ul');
    let block_data = [block_id,timestamp,receiver,sender,amount,total,prev_hash,hash];
    let temp_data = ['BlockID :','Timestamp :','Receiver :','Sender :','Amount :','Total :','Previous Hash :','Hash :']
    div_block.classList.add('block');
    for(let count = 0; count < 8; count++){
        let li = document.createElement('li');
        li.textContent = temp_data[count]+block_data[count];
        ul.append(li);
    }

    div_block.append(ul);
    let position = document.getElementById('user'+String(person+1));
    position.insertAdjacentElement('beforeend',div_block);
}

socket.on('new-transaction', ({ data1,data2 }) => {
    for( user of [data1,data2]){
        createBlockHTML(user[0].block_id,user[0].timestamp,user[0].receiver,user[0].sender,user[0].amount,user[0].total,user[0].prev_hash,user[0].hash,user[1])
    };
});

// TO-DO
// --> Get all DATA