import React, { useState, useEffect } from 'react';
import './Calculator.css';

const Calculator = () => {
  const [display, setDisplay] = useState('0');
  const [previousValue, setPreviousValue] = useState(null);
  const [operation, setOperation] = useState(null);
  const [waitingForOperand, setWaitingForOperand] = useState(false);
  const [history, setHistory] = useState([]);
  const [theme, setTheme] = useState('light');

  const themes = {
    light: {
      background: '#ffffff',
      display: '#f8f9fa',
      button: '#e9ecef',
      buttonHover: '#dee2e6',
      text: '#212529',
      operation: '#007bff',
      equals: '#28a745'
    },
    dark: {
      background: '#212529',
      display: '#343a40',
      button: '#495057',
      buttonHover: '#6c757d',
      text: '#ffffff',
      operation: '#0d6efd',
      equals: '#198754'
    },
    neon: {
      background: '#0a0a0a',
      display: '#1a1a1a',
      button: '#2a2a2a',
      buttonHover: '#3a3a3a',
      text: '#00ff00',
      operation: '#ff00ff',
      equals: '#00ffff'
    }
  };

  useEffect(() => {
    document.documentElement.style.setProperty('--bg-color', themes[theme].background);
    document.documentElement.style.setProperty('--display-color', themes[theme].display);
    document.documentElement.style.setProperty('--button-color', themes[theme].button);
    document.documentElement.style.setProperty('--button-hover', themes[theme].buttonHover);
    document.documentElement.style.setProperty('--text-color', themes[theme].text);
    document.documentElement.style.setProperty('--operation-color', themes[theme].operation);
    document.documentElement.style.setProperty('--equals-color', themes[theme].equals);
  }, [theme]);

  const inputNumber = (num) => {
    if (waitingForOperand) {
      setDisplay(String(num));
      setWaitingForOperand(false);
    } else {
      setDisplay(display === '0' ? String(num) : display + num);
    }
  };

  const inputDecimal = () => {
    if (waitingForOperand) {
      setDisplay('0.');
      setWaitingForOperand(false);
    } else if (display.indexOf('.') === -1) {
      setDisplay(display + '.');
    }
  };

  const clear = () => {
    setDisplay('0');
    setPreviousValue(null);
    setOperation(null);
    setWaitingForOperand(false);
  };

  const performOperation = (nextOperation) => {
    const inputValue = parseFloat(display);

    if (previousValue === null) {
      setPreviousValue(inputValue);
    } else if (operation) {
      const currentValue = previousValue || 0;
      const newValue = calculate(currentValue, inputValue, operation);

      setDisplay(String(newValue));
      setPreviousValue(newValue);
      
      // Add to history
      const historyEntry = `${currentValue} ${operation} ${inputValue} = ${newValue}`;
      setHistory(prev => [...prev.slice(-9), historyEntry]);
    }

    setWaitingForOperand(true);
    setOperation(nextOperation);
  };

  const calculate = (firstValue, secondValue, operation) => {
    switch (operation) {
      case '+':
        return firstValue + secondValue;
      case '-':
        return firstValue - secondValue;
      case '×':
        return firstValue * secondValue;
      case '÷':
        return secondValue !== 0 ? firstValue / secondValue : 0;
      case '%':
        return firstValue % secondValue;
      case '^':
        return Math.pow(firstValue, secondValue);
      default:
        return secondValue;
    }
  };

  const calculateResult = () => {
    const inputValue = parseFloat(display);

    if (previousValue !== null && operation) {
      const newValue = calculate(previousValue, inputValue, operation);
      setDisplay(String(newValue));
      setPreviousValue(null);
      setOperation(null);
      setWaitingForOperand(true);
    }
  };

  const handleKeyPress = (event) => {
    const { key } = event;
    
    if (key >= '0' && key <= '9') {
      inputNumber(parseInt(key));
    } else if (key === '.') {
      inputDecimal();
    } else if (key === '+') {
      performOperation('+');
    } else if (key === '-') {
      performOperation('-');
    } else if (key === '*') {
      performOperation('×');
    } else if (key === '/') {
      event.preventDefault();
      performOperation('÷');
    } else if (key === 'Enter' || key === '=') {
      calculateResult();
    } else if (key === 'Escape' || key === 'c' || key === 'C') {
      clear();
    }
  };

  useEffect(() => {
    window.addEventListener('keydown', handleKeyPress);
    return () => window.removeEventListener('keydown', handleKeyPress);
  }, [display, previousValue, operation, waitingForOperand]);

  const scientificFunctions = {
    sqrt: () => {
      const value = parseFloat(display);
      if (value >= 0) {
        setDisplay(String(Math.sqrt(value)));
        setWaitingForOperand(true);
      }
    },
    square: () => {
      const value = parseFloat(display);
      setDisplay(String(value * value));
      setWaitingForOperand(true);
    },
    sin: () => {
      const value = parseFloat(display);
      setDisplay(String(Math.sin(value * Math.PI / 180)));
      setWaitingForOperand(true);
    },
    cos: () => {
      const value = parseFloat(display);
      setDisplay(String(Math.cos(value * Math.PI / 180)));
      setWaitingForOperand(true);
    },
    tan: () => {
      const value = parseFloat(display);
      setDisplay(String(Math.tan(value * Math.PI / 180)));
      setWaitingForOperand(true);
    },
    log: () => {
      const value = parseFloat(display);
      if (value > 0) {
        setDisplay(String(Math.log10(value)));
        setWaitingForOperand(true);
      }
    },
    ln: () => {
      const value = parseFloat(display);
      if (value > 0) {
        setDisplay(String(Math.log(value)));
        setWaitingForOperand(true);
      }
    },
    factorial: () => {
      const value = parseInt(display);
      if (value >= 0 && value <= 170) {
        let result = 1;
        for (let i = 2; i <= value; i++) {
          result *= i;
        }
        setDisplay(String(result));
        setWaitingForOperand(true);
      }
    }
  };

  return (
    <div className="calculator-container">
      <div className="calculator-header">
        <h1>Advanced Calculator</h1>
        <div className="theme-selector">
          <button 
            className={`theme-btn ${theme === 'light' ? 'active' : ''}`}
            onClick={() => setTheme('light')}
          >
            ☀️
          </button>
          <button 
            className={`theme-btn ${theme === 'dark' ? 'active' : ''}`}
            onClick={() => setTheme('dark')}
          >
            🌙
          </button>
          <button 
            className={`theme-btn ${theme === 'neon' ? 'active' : ''}`}
            onClick={() => setTheme('neon')}
          >
            ⚡
          </button>
        </div>
      </div>

      <div className="calculator">
        <div className="display">
          <div className="display-value">{display}</div>
          <div className="display-operation">
            {previousValue !== null && operation ? `${previousValue} ${operation}` : ''}
          </div>
        </div>

        <div className="calculator-grid">
          {/* Scientific Functions Row */}
          <button className="function-btn" onClick={scientificFunctions.sqrt}>√</button>
          <button className="function-btn" onClick={scientificFunctions.square}>x²</button>
          <button className="function-btn" onClick={scientificFunctions.sin}>sin</button>
          <button className="function-btn" onClick={scientificFunctions.cos}>cos</button>
          <button className="function-btn" onClick={scientificFunctions.tan}>tan</button>

          <button className="function-btn" onClick={scientificFunctions.log}>log</button>
          <button className="function-btn" onClick={scientificFunctions.ln}>ln</button>
          <button className="function-btn" onClick={scientificFunctions.factorial}>n!</button>
          <button className="operation-btn" onClick={() => performOperation('^')}>x^y</button>
          <button className="operation-btn" onClick={() => performOperation('%')}>%</button>

          {/* Main Calculator */}
          <button className="clear-btn" onClick={clear}>C</button>
          <button className="operation-btn" onClick={() => performOperation('÷')}>÷</button>
          <button className="operation-btn" onClick={() => performOperation('×')}>×</button>
          <button className="operation-btn" onClick={() => performOperation('-')}>-</button>

          <button className="number-btn" onClick={() => inputNumber(7)}>7</button>
          <button className="number-btn" onClick={() => inputNumber(8)}>8</button>
          <button className="number-btn" onClick={() => inputNumber(9)}>9</button>
          <button className="operation-btn" onClick={() => performOperation('+')}>+</button>

          <button className="number-btn" onClick={() => inputNumber(4)}>4</button>
          <button className="number-btn" onClick={() => inputNumber(5)}>5</button>
          <button className="number-btn" onClick={() => inputNumber(6)}>6</button>
          <button className="equals-btn" onClick={calculateResult} rowSpan="2">=</button>

          <button className="number-btn" onClick={() => inputNumber(1)}>1</button>
          <button className="number-btn" onClick={() => inputNumber(2)}>2</button>
          <button className="number-btn" onClick={() => inputNumber(3)}>3</button>

          <button className="number-btn zero-btn" onClick={() => inputNumber(0)}>0</button>
          <button className="number-btn" onClick={inputDecimal}>.</button>
        </div>

        {history.length > 0 && (
          <div className="history">
            <h3>History</h3>
            <div className="history-list">
              {history.map((entry, index) => (
                <div key={index} className="history-entry">{entry}</div>
              ))}
            </div>
            <button className="clear-history-btn" onClick={() => setHistory([])}>
              Clear History
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

export default Calculator;
