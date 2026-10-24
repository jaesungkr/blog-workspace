const path = require('node:path');
const { toCsv } = require(path.join(__dirname, 'fixture/notes-example/csv.js'));
const cases = [
  {name: 'plain', input: [{id: 1, title: 'First note'}], expected: 'id,title\n1,"First note"\n'},
  {name: 'comma-and-quotes', input: [{id: 1, title: 'Hello, "REA"'}], expected: 'id,title\n1,"Hello, ""REA"""\n'},
  {name: 'korean', input: [{id: 2, title: '서울, "메모"'}], expected: 'id,title\n2,"서울, ""메모"""\n'},
  {name: 'embedded-newline', input: [{id: 3, title: '첫째 줄\n둘째 줄'}], expected: 'id,title\n3,"첫째 줄\n둘째 줄"\n'},
  {name: 'empty-list', input: [], expected: 'id,title\n'}
];
const results = cases.map(c => ({...c, actual: toCsv(c.input), pass: toCsv(c.input) === c.expected}));
process.stdout.write(JSON.stringify({actor: 'Codex', method: 'Call the unmodified official toCsv function; compare exact strings fixed before execution.', results}, null, 2) + '\n');
if (results.some(c => !c.pass)) process.exitCode = 1;
