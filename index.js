let instruction;
// max number ah can hold is 255
// FF in hex = 255 in decimal = 11111111 in binary
let opCodes = ["mov", "add", "sub", "div", "inc", "dec"];
let generalRegisters = ["ah", "bh", "ch", "dh", "al", "bl", "cl", "dl"];
let generalValues = ["0", "0", "0", "0", "0", "0", "0", "0"];
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

function executer_small(instruction) {
  let bigReg = ["ax", "bx", "cx", "dx"];
  if (instruction[0] === "mov") {
    if (
      // if destination is a register and source is a register
      opCodes.includes(instruction[0]) &&
      generalRegisters.includes(instruction[1]) &&
      generalRegisters.includes(instruction[2])
      
    ) {
      let dest = instruction[1];
      let source = instruction[2];
      let dest_index = generalRegisters.indexOf(dest);
      let source_index = generalRegisters.indexOf(source);
      generalValues[dest_index] = generalValues[source_index];
      all_value_initial();
    } else if (
      // if destination is a register and source is a memory place
      opCodes.includes(instruction[0]) &&
      generalRegisters.includes(instruction[1]) &&
      memoryPlaces.includes(instruction[2])
    ) {
      let dest = instruction[1];
      let source = instruction[2];
      let dest_index = generalRegisters.indexOf(dest);
      let source_index = memoryPlaces.indexOf(source);
      generalValues[dest_index] = memoryValues[source_index];
      all_value_initial();
    } else if (
      // if destination is a memory place and source is a register
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
    } else if (
      // if destination is a memory place and source is a memory place
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
      toString(generalValues[dest_index]);
      all_value_initial();
    }
  } else if (instruction[0] === "add") {
    if (
      // if destination is a register and source is a register
      opCodes.includes(instruction[0]) &&
      generalRegisters.includes(instruction[1]) &&
      generalRegisters.includes(instruction[2])
    ) {
      let dest = instruction[1];
      let source = instruction[2];
      let dest_index = generalRegisters.indexOf(dest);
      let source_index = generalRegisters.indexOf(source);
      generalValues[dest_index] =
        parseInt(generalValues[dest_index]) +
        parseInt(generalValues[source_index], 16);
      all_value_initial();
    } else if (
      // if destination is a register and source is a memory place
      opCodes.includes(instruction[0]) &&
      generalRegisters.includes(instruction[1]) &&
      memoryPlaces.includes(instruction[2])
    ) {
      let dest = instruction[1];
      let source = instruction[2];
      let dest_index = generalRegisters.indexOf(dest);
      let source_index = memoryPlaces.indexOf(source);
      generalValues[dest_index] =
        parseInt(generalValues[dest_index]) +
        parseInt(memoryValues[source_index]);
      all_value_initial();
    } else if (
      opCodes.includes(instruction[0]) &&
      generalRegisters.includes(instruction[1]) &&
      !isNaN(instruction[2]) //if source is a number
    ) {
      let dest = instruction[1];
      let source = instruction[2];
      let dest_index = generalRegisters.indexOf(dest);
      generalValues[dest_index] =
        parseInt(generalValues[dest_index]) + parseInt(source);
      all_value_initial();
    }
  } else if (instruction[0] === "sub") {
    if (
      // if destination is a register and source is a register
      opCodes.includes(instruction[0]) &&
      generalRegisters.includes(instruction[1]) &&
      generalRegisters.includes(instruction[2])
    ) {
      let dest = instruction[1];
      let source = instruction[2];
      let dest_index = generalRegisters.indexOf(dest);
      let source_index = generalRegisters.indexOf(source);
      generalValues[dest_index] =
        parseInt(generalValues[dest_index]) -
        parseInt(generalValues[source_index]);
      all_value_initial();
    } else if (
      // if destination is a register and source is a memory place
      opCodes.includes(instruction[0]) &&
      generalRegisters.includes(instruction[1]) &&
      memoryPlaces.includes(instruction[2])
    ) {
      let dest = instruction[1];
      let source = instruction[2];
      let dest_index = generalRegisters.indexOf(dest);
      let source_index = memoryPlaces.indexOf(source);
      generalValues[dest_index] =
        parseInt(generalValues[dest_index]) -
        parseInt(memoryValues[source_index]);
      all_value_initial();
    } else if (
      opCodes.includes(instruction[0]) &&
      generalRegisters.includes(instruction[1]) &&
      !isNaN(instruction[2]) //if source is a number
    ) {
      let dest = instruction[1];
      let source = instruction[2];
      let dest_index = generalRegisters.indexOf(dest);
      generalValues[dest_index] =
        parseInt(generalValues[dest_index]) - parseInt(source);
      all_value_initial();
    }
  } else if (instruction[0] === "mul") {
    if (
      // if destination is a register and source is a register
      opCodes.includes(instruction[0]) &&
      generalRegisters.includes(instruction[1]) &&
      generalRegisters.includes(instruction[2])
    ) {
      let dest = instruction[1];
      let source = instruction[2];
      let dest_index = generalRegisters.indexOf(dest);
      let source_index = generalRegisters.indexOf(source);
      generalValues[dest_index] =
        parseInt(generalValues[dest_index]) *
        parseInt(generalValues[source_index]);
      all_value_initial();
    } else if (
      // if destination is a register and source is a memory place
      opCodes.includes(instruction[0]) &&
      generalRegisters.includes(instruction[1]) &&
      memoryPlaces.includes(instruction[2])
    ) {
      let dest = instruction[1];
      let source = instruction[2];
      let dest_index = generalRegisters.indexOf(dest);
      let source_index = memoryPlaces.indexOf(source);
      generalValues[dest_index] =
        parseInt(generalValues[dest_index]) *
        parseInt(memoryValues[source_index]);
      all_value_initial();
    } else if (
      opCodes.includes(instruction[0]) &&
      generalRegisters.includes(instruction[1]) &&
      !isNaN(instruction[2]) //if source is a number
    ) {
      let dest = instruction[1];
      let source = instruction[2];
      let dest_index = generalRegisters.indexOf(dest);
      generalValues[dest_index] =
        parseInt(generalValues[dest_index]) * parseInt(source);
      all_value_initial();
    }
  } else if (instruction[0] === "div") {
    if (
      // if destination is a register and source is a register
      opCodes.includes(instruction[0]) &&
      generalRegisters.includes(instruction[1]) &&
      generalRegisters.includes(instruction[2])
    ) {
      let dest = instruction[1];
      let source = instruction[2];
      let dest_index = generalRegisters.indexOf(dest);
      let source_index = generalRegisters.indexOf(source);
      generalValues[dest_index] =
        parseInt(generalValues[dest_index]) /
        parseInt(generalValues[source_index]);
      all_value_initial();
    } else if (
      // if destination is a register and source is a memory place
      opCodes.includes(instruction[0]) &&
      generalRegisters.includes(instruction[1]) &&
      memoryPlaces.includes(instruction[2])
    ) {
      let dest = instruction[1];
      let source = instruction[2];
      let dest_index = generalRegisters.indexOf(dest);
      let source_index = memoryPlaces.indexOf(source);
      generalValues[dest_index] =
        parseInt(generalValues[dest_index]) /
        parseInt(memoryValues[source_index]);
      all_value_initial();
    } else if (
      opCodes.includes(instruction[0]) &&
      generalRegisters.includes(instruction[1]) &&
      !isNaN(instruction[2]) //if source is a number
    ) {
      let dest = instruction[1];
      let source = instruction[2];
      let dest_index = generalRegisters.indexOf(dest);
      generalValues[dest_index] =
        parseInt(generalValues[dest_index]) / parseInt(source);
      all_value_initial();
    }
  } else if (instruction[0] === "inc") {
    if (
      // if destination is a register and source is a register
      opCodes.includes(instruction[0]) &&
      generalRegisters.includes(instruction[1])
    ) {
      let dest = instruction[1];
      let dest_index = generalRegisters.indexOf(dest);
      generalValues[dest_index] = parseInt(generalValues[dest_index]) + 1;
      all_value_initial();
    } else if (
      // if destination is a register and source is a memory place
      opCodes.includes(instruction[0]) &&
      memoryPlaces.includes(instruction[1])
    ) {
      let dest = instruction[1];
      let dest_index = memoryPlaces.indexOf(dest);
      memoryValues[dest_index] = parseInt(memoryValues[dest_index]) + 1;
      all_value_initial();
    }
  } else if (instruction[0] === "dec") {
    if (
      // if destination is a register and source is a register
      opCodes.includes(instruction[0]) &&
      generalRegisters.includes(instruction[1])
    ) {
      let dest = instruction[1];
      let dest_index = generalRegisters.indexOf(dest);
      generalValues[dest_index] = parseInt(generalValues[dest_index]) - 1;
      all_value_initial();
    } else if (
      // if destination is a register and source is a memory place
      opCodes.includes(instruction[0]) &&
      memoryPlaces.includes(instruction[1])
    ) {
      let dest = instruction[1];
      let dest_index = memoryPlaces.indexOf(dest);
      memoryValues[dest_index] = parseInt(memoryValues[dest_index]) - 1;
      all_value_initial();
    }
  }
}

all_value_initial();

function syntax_validater(instruction) {
  let bigReg = ["ax", "bx", "cx", "dx"];
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

  if (generalRegisters.includes(instruction[1]) && !isNaN(instruction[2])) {
    flag_source = true;
  }

  if (bigReg.includes(instruction[1]) && !isNaN(instruction[2])) {
    flag_dest = true;
    flag_source = true;

    if (instruction[2] > 255) {
      flag_source = false;
    }

    if (instruction[2] < 0) {
      flag_source = false;
    }
  }

  if (instruction[0] === "inc" || instruction[0] === "dec") {
    if (
      generalRegisters.includes(instruction[1]) ||
      memoryPlaces.includes(instruction[1])
    ) {
      flag_dest = true;
      flag_source = true;
    }
  }

  // for debugging
  console.log(flag_op, flag_dest, flag_source);
  
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
  syntax_validater(instruction);
  executer_small(instruction);
}
