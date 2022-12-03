let instruction;


let opCodes = ["mov","add","sub","div","inc","dec"];
let generalRegisters= ["ah","al","bh","bl","ch","cl","dh","dl"];
let memoryPlaces = ["[0h]","[1h]","[2h]","[3h]","[4h]","[5h]","[6h]","[7h]","[8h]","[9h]","[ah]","[bh]","[ch]","[dh]","[eh]","[fh]"]



function validater(instruction){
    let flag_op = false;
    let flag_dest = false;
    let flag_source = false;

    flag_op = opCodes.includes(instruction[0]);
    if (generalRegisters.includes(instruction[1]) || memoryPlaces.includes(instruction[1])) {
        flag_dest = true;
    }

    if (generalRegisters.includes(instruction[2]) || memoryPlaces.includes(instruction[2])) {
        flag_source = true;
    }
    
    console.log(flag_op);
    console.log(flag_dest);
    console.log(flag_source);

    if(flag_op==false || flag_dest==false || flag_source==false){
        // alert("YOUR MOTHER HUNG HERSELF");
        document.getElementById("text_field").value = "Invalid Instruction";
    }
}

function cleaner_tokenizer(instruction){
    instruction = instruction.replace(","," ");
    instruction = instruction.replace(/  +/g," ");
    let tokens = instruction.split(" ");
    return tokens;
}

function execute_button(){
    instruction = document.getElementById("text_field").value; //string instruction
    instruction = cleaner_tokenizer(instruction);
    console.log(instruction);
    validater(instruction);
}



