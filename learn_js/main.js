courses= [
  { name: 'Javascript', coin: 1000 },
  { name: 'PHP', coin: 1200 },
  { name: 'Dart', coin: 1400 }
]
function run(courses) {
  var totolcoin = courses.reduce(function(totol, courses){
      return totol + courses.coin;
  },0)
  console.log(totolcoin)

}
run(courses)