// Big O is a numeric representation of the performance of code
  // discuss trade offs
  // pinpoint code inefficiences

// you can use timers to check performance
  // performance.now() checks current run time of window
  // var t1 = performance.now()
  // call function ()
  // var t2 = performance.now()
  // console.log(`Time Elapsed: ${(t2 - t1) / 1000} seconds.`);


// Problem with time:

  //machines record at different times
  // fast algorithims are tough to compare

// Count Operations

  //one way of comparing time:

    // operations = + - * /
    // loops repeat operations


// Big O run time:

  //O(1) constant time

  //O(N) - Time grows as N  grows - loops not nested

  //O(n^2) - Quadratic grows roughly as n^2


// Big O Short Hands

  // Arithmetic operations are constant
  // variable assignment is constant
  // accessing elements in an array by key or index is constant time
  // loop = length of loop times the complexity of loop

// Method used Math.min() takes in multiple numbers or spread array as parameter return smallest



// Space Complexity
  // amount of memory allocation

  //auxiliary space complexity - whats happening inside of the algorithim

  // Most primitives are constant space booleans numbers undefined null
  // strings O(N) Space
  // Reference types are O(N) arrays : n is length objects n is keys


  //O(1) space is constant
  //O(N) space grows relative to N


// Logarithims

  //O(log n) faster than O(N) slower than constant time

    // Searching algorithims
    //Sorting algorithims
    //Recursion
