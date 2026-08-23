/**
 * @param {Promise<number>} promise1
 * @param {Promise<number>} promise2
 * @return {Promise<number>}
 */
var addTwoPromises = async function(promise1, promise2) {
    const num1 = await promise1;
    const num2 = await promise2;

    return num1 + num2;
};