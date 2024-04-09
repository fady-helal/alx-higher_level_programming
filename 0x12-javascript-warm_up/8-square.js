#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
    console.log('Missing size');
}
for (let i = 0; i < Number(process.argv[2]); i++){
    for (let i = 0; i < Number(process.argv[2]); i++){
        process.stdout.write('X');
    }
    console.log();
}