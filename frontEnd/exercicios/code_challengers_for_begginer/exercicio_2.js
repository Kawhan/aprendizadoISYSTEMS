// Print a table containing multiplication tables
let valor_initial = 1;
let len_tables = 10;

for (let i = valor_initial; i <= len_tables; i++) {
    for (let j = valor_initial; j <= len_tables; j++) {
        console.log(`O valor de ${i} * ${j} = ${i * j}`);
    }
    console.log("=====================");
}
