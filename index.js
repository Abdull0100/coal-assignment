let instruction;

let opCodes = ["mov", "add", "sub", "div", "inc", "dec"];
let generalRegisters = ["ah", "bh", "ch", "dh", "al", "bl", "cl", "dl"];
let generalValues = ["0", "3", "0", "0", "0", "0", "0", "0"];
let memoryPlaces = [
  "[0h]",
  "[1h]",
  "[2h]",
  "[3h]",
  "[4h]",
  "[5h]",
  "[6h]",
  "[7h]",
  "[8h]",
  "[9h]",
  "[ah]",
  "[bh]",
  "[ch]",
  "[dh]",
  "[eh]",
  "[fh]",
];
let memoryValues = [
  "0",
  "0",
  "0",
  "0",
  "0",
  "0",
  "0",
  "0",
  "0",
  "0",
  "0",
  "0",
  "0",
  "0",
  "0",
  "0",
];

function all_value_initial() {
  //for memory places
  for (let i = 0; i < 16; i++) {
    document.getElementById(`name${i}`).innerHTML =
      memoryPlaces[i].toUpperCase();
    document.getElementById(`value${i}`).innerHTML = memoryValues[i];
  }

  //for high registers
  for (let i = 0; i < 4; i++) {
    document.getElementById(`${i}H`).innerHTML = generalValues[i];
  }

  //for low registers
  for (let i = 0; i < 4; i++) {
    document.getElementById(`${i}L`).innerHTML = generalValues[i + 4];
  }
}

function executer(instruction) {
  if (instruction[0] === "mov") {
    if ( // if destination is a register and source is a register
      opCodes.includes(instruction[0]) &&
      generalRegisters.includes(instruction[1]) &&
      generalRegisters.includes(instruction[2])
    ) {
      let dest = instruction[1];
      let source = instruction[2];
      let dest_index = generalRegisters.indexOf(dest);
      let source_index = generalRegisters.indexOf(source);
      generalValues[dest_index] = generalValues[source_index];
      document.getElementById(
        `${Math.floor(dest_index / 4)}${dest_index % 4 == 0 ? "H" : "L"}`
      ).innerHTML = generalValues[dest_index];
    } else if ( // if destination is a register and source is a memory place
      opCodes.includes(instruction[0]) &&
      generalRegisters.includes(instruction[1]) &&
      memoryPlaces.includes(instruction[2])
    ) {
      let dest = instruction[1];
      let source = instruction[2];
      let dest_index = generalRegisters.indexOf(dest);
      let source_index = memoryPlaces.indexOf(source);
      generalValues[dest_index] = memoryValues[source_index];
      document.getElementById(
        `${Math.floor(dest_index / 4)}${dest_index % 4 == 0 ? "H" : "L"}`
      ).innerHTML = generalValues[dest_index];
    } else if ( // if destination is a memory place and source is a register
      opCodes.includes(instruction[0]) &&
      memoryPlaces.includes(instruction[1]) &&
      generalRegisters.includes(instruction[2])
    ) {
      let dest = instruction[1];
      let source = instruction[2];
      let dest_index = memoryPlaces.indexOf(dest);
      let source_index = generalRegisters.indexOf(source);
      memoryValues[dest_index] = generalValues[source_index];
      document.getElementById(`value${dest_index}`).innerHTML =
        memoryValues[dest_index];
    } else if (  // if destination is a memory place and source is a memory place
      opCodes.includes(instruction[0]) &&
      memoryPlaces.includes(instruction[1]) &&
      memoryPlaces.includes(instruction[2])
    ) {
      alert("Invalid Instruction"); //direct memory to memory not allowed
    } else if (
        opCodes.includes(instruction[0]) &&
        generalRegisters.includes(instruction[1]) &&
        !isNaN(instruction[2]) //if source is a number
        ) {
        let dest = instruction[1];
        let source = instruction[2];
        let dest_index = generalRegisters.indexOf(dest);
        generalValues[dest_index] = source;
        document.getElementById(
            `${Math.floor(dest_index / 4)}${dest_index % 4 == 0 ? "H" : "L"}`
        ).innerHTML = generalValues[dest_index];
        }
  }
}

all_value_initial();

function validater(instruction) {
  let flag_op = false;
  let flag_dest = false;
  let flag_source = false;

  flag_op = opCodes.includes(instruction[0]);
  if (
    generalRegisters.includes(instruction[1]) ||
    memoryPlaces.includes(instruction[1])
  ) {
    flag_dest = true;
  }

  if (
    generalRegisters.includes(instruction[2]) ||
    memoryPlaces.includes(instruction[2])
  ) {
    flag_source = true;
  }

  console.log(flag_op);
  console.log(flag_dest);
  console.log(flag_source);

  if (flag_op == false || flag_dest == false || flag_source == false) {
    document.getElementById("text_field").value = "";
    alert("Invalid Instruction");
  }
}

function cleaner_tokenizer(instruction) {
  instruction = instruction.replace(",", " ");
  instruction = instruction.replace(/  +/g, " ");
  let tokens = instruction.split(" ");
  return tokens;
}

function execute_button() {
  instruction = document.getElementById("text_field").value; //string instruction
  instruction = cleaner_tokenizer(instruction);
  console.log(instruction);
  validater(instruction);
  executer(instruction);
}
