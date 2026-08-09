function createCounter(n: number): () => number {
    // Store the initial value in a closure variable
    let currentValue: number = n;
  
    // Return a function that captures the currentValue variable
    return function(): number {
        // Return the current value and then increment it (post-increment)
        return currentValue++;
    };
}

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */