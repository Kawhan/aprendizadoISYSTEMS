//Lidando com promessas rejeitadas

// Manipular rejeitado Promisesem bloco try.

var response = await promisedFunction().catch((err) => {
    console.error(err);
});
// response will be undefined if the promise is rejected
