"use strict";
// Set this variable to true to publicly expose otherwise private functions inside of SudokuSolver

var TESTABLE = true;
var SudokuSolver = (function (testable) {
  var solver;

  function solve(boardString) {
    var boardArray = boardString.split("");
    if (boardIsInvalid(boardArray)) {
      return false;
    }
    let BoardArray = my_helper(0, boardArray);
    let s = "";
    for (let i = 0; i < 81; i++) {
      s += BoardArray[i];
    }
    return s;
  }

  function boardIsInvalid(boardArray) {
    return !boardIsValid(boardArray);
  }

  function boardIsValid(boardArray) {
    return (
      allRowsValid(boardArray) &&
      allColumnsValid(boardArray) &&
      allBoxesValid(boardArray)
    );
  }

  function allRowsValid(boardArray) {
    return [0, 9, 18, 27, 36, 45, 54, 63, 72]
      .map(function (i) {
        return getRow(boardArray, i);
      })
      .reduce(function (validity, row) {
        return collectionIsValid(row) && validity;
      }, true);
  }

  function getRow(boardArray, i) {
    var startingEI = Math.floor(i / 9) * 9;
    return boardArray.slice(startingEI, startingEI + 9);
  }

  function allColumnsValid(boardArray) {
    for (let i = 0; i < 9; i++) {
      let numCounts = {};
      for (let j = i; j <= 72 + i; j += 9) {
        if (boardArray[j] != "-") {
          if (numCounts[boardArray[j]] == undefined) {
            numCounts[boardArray[j]] = 1;
          } else {
            return false;
          }
        }
      }
    }
    return true;
  }

  function allBoxesValid(boardArray) {
    let arr = [0, 3, 6, 27, 30, 33, 54, 57, 60];
    for (let x = 0; x < arr.length; x++) {
      let i = arr[x];
      let countnum = {};
      for (let j = i; j < i + 3; j++) {
        for (let k = j; k < j + 27; k += 9) {
          if (boardArray[k] != "-") {
            if (countnum[boardArray[k]] == undefined) {
              countnum[boardArray[k]] = 1;
            } else {
              return false;
            }
          }
        }
      }
    }
    return true;
  }

  function my_helper(i, boardArray) {
    if (i >= 81) return boardArray;
    let ans;
    if (boardArray[i] == "-") {
      for (let val = "1"; val <= "9"; val++) {
        let s = "";
        s += val;
        boardArray[i] = s;
        if (boardIsValid(boardArray)) {
          ans = my_helper(i + 1, boardArray);
          if (ans) return ans;
        }
        boardArray[i] = "-";
      }
    } else {
      ans = my_helper(i + 1, boardArray);
      if (ans) return ans;
    }
    return false;
  }

  function collectionIsValid(collection) {
    var numCounts = {};
    for (var i = 0; i < collection.length; i++) {
      if (collection[i] != "-") {
        if (numCounts[collection[i]] == undefined) {
          numCounts[collection[i]] = 1;
        } else {
          return false;
        }
      }
    }
    return true;
  }
  if (testable) {
    // These methods will be exposed publicly when testing is on.
    solver = {
      solve: solve,
      boardIsInvalid: boardIsInvalid,
      boardIsValid: boardIsValid,
      allRowsValid: allRowsValid,
      getRow: getRow,
      allColumnsValid: allColumnsValid,
      allBoxesValid: allBoxesValid,
      collectionIsValid: collectionIsValid,
      toString: toString,
    };
  } else {
    solver = { solve: solve };
  }
  return solver;
})(TESTABLE);
