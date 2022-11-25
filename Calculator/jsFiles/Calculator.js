// DOM Elements
const Display = document.querySelector('.display');

const AC = document.querySelector('[Clear-all]');
const ChangeSign = document.querySelector('[Change-sign]');
const CalPercentage = document.querySelector('[Calculate-percentage]');
const Div = document.querySelector('[Division]');
const Mul = document.querySelector('[Multiplication]');
const Subtract = document.querySelector('[Subtraction]');
const Addition = document.querySelector('[Addition]');
const Equals = document.querySelector('[Equals]');

const Decimal = document.querySelector('[Decimal]');
const Number0 = document.querySelectorAll('[Number0]');
const Number1 = document.querySelectorAll('[Number1]');
const Number2 = document.querySelectorAll('[Number2]');
const Number3 = document.querySelectorAll('[Number3]');
const Number4 = document.querySelectorAll('[Number4]');
const Number5 = document.querySelectorAll('[Number5]');
const Number6 = document.querySelectorAll('[Number6]');
const Number7 = document.querySelectorAll('[Number7]');
const Number8 = document.querySelectorAll('[Number8]');
const Number9 = document.querySelectorAll('[Number9]');
const NumberArray = [Number0, Number1, Number2, Number3, Number4, Number5, Number6, Number7, Number8, Number9];



// Variables
let valueStringInMemory = null;
let operatorInMemory = null;



// Functions
const getValueAsString = () => {
    const currentDisplayStr = Display.textContent
    return currentDisplayStr.split(",").join("");    // get rid of commas
}


const getValueAsNum = () => {
    return parseFloat(getValueAsString());    // get rid of commas
}

const setStrAsValue = (valueStr) => {
    // To prevent the comma be removed
    if (valueStr[valueStr.length-1]===".")
    {
        Display.textContent+=".";
        return;
    }
    const [wholeNumStr, decimalStr] = valueStr.split('.');  // split the floating part and th whole part
    if (decimalStr)
    {
        Display.textContent = parseFloat(wholeNumStr).toLocaleString() + "." + decimalStr;
    }
    else
    {
        Display.textContent = parseFloat(valueStr).toLocaleString();
        // automatically put comma in "thousand"
        // 1,000
    }
}

const handleNumberClick = (NumStr) => {
    const currentDisplayStr = getValueAsString();
    if (currentDisplayStr === '0') {
        setStrAsValue(NumStr);
    } 
    else 
    {
        setStrAsValue(currentDisplayStr+NumStr);
    }
}

const getResultOfOperationAsString = () => {
    const currentValueNum = getValueAsNum();
    const valueNumInMemory = parseFloat(valueStringInMemory);
    let newValueAsNum;
    if (operatorInMemory==='Addition')
    {
        newValueAsNum = valueNumInMemory + currentValueNum;
    }
    else if (operatorInMemory==='Subtraction')
    {
        newValueAsNum = valueNumInMemory - currentValueNum;
    }
    else if (operatorInMemory==='Mul')
    {
        newValueAsNum = valueNumInMemory * currentValueNum;
    }
    else if (operatorInMemory==='Div')
    {
        newValueAsNum = valueNumInMemory / currentValueNum;
    }   
    return  newValueAsNum.toString();
}

const handleOperatorClick = (operation) => {
    const currentValueString = getValueAsString();


    // No number in memory ---- store it in memory, set number on the screen to 0
    if (!valueStringInMemory)
    {
        valueStringInMemory = currentValueString;
        operatorInMemory = operation;
        setStrAsValue('0');
        return;
    }

    // A number in memory ---- do the operation
    valueStringInMemory = getResultOfOperationAsString();
    operatorInMemory = operation;
    setStrAsValue('0');
}



// Add event listener to functions
AC.addEventListener('click', () => {
    setStrAsValue("0");
    valueStringInMemory = null;
    operatorInMemory = null;
});

ChangeSign.addEventListener('click', () => {
    const currentValNum = getValueAsNum();
    const currentValStr = getValueAsString();

    if (currentValStr === '-0')
    {
        setStrAsValue('0');
        return;
    }

    if (currentValNum >= 0)
    {
        setStrAsValue('-' + currentValStr);
    }
    else
    {
        setStrAsValue(currentValStr.substring(1));
    }
});

CalPercentage.addEventListener('click', () => {
    const currentValNum = getValueAsNum();
    const newValueNum = currentValNum/100;
    setStrAsValue(newValueNum.toString());
    valueStringInMemory = null;
    operatorInMemory = null;
});



// Add Event Listeners to operators
Div.addEventListener('click', ()=>{
    handleOperatorClick('Div');
});

Mul.addEventListener('click', ()=>{
    handleOperatorClick('Mul');
});

Subtract.addEventListener('click', ()=>{
    handleOperatorClick('Subtraction');
});

Addition.addEventListener('click', ()=>{
    handleOperatorClick('Addition');
});

Equals.addEventListener('click', ()=>{
    if (valueStringInMemory)
    {
        setStrAsValue(getResultOfOperationAsString());
        valueStringInMemory = null;
        operatorInMemory = null;
    }
});



// Add Event Listeners to numbers and decimal
for (let i=0; i < NumberArray.length; i++) 
{
    const numberEl = NumberArray[i];
    numberEl[0].addEventListener('click', () => {
      handleNumberClick(i.toString());
    });
}

Decimal.addEventListener('click', ()=>{
    const currentDisplayStr = getValueAsString();
    if (!currentDisplayStr.includes("."))
    {
        setStrAsValue(currentDisplayStr + '.');
    }
});







