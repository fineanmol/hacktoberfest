class Person {
    constructor (name='Anyonymous', location='Unknown') {
      this.name = name;
      this.place = location;
    }
    greeting (name=this.name, place=this.place) {
      let str = "Hello, World! by " + name + " from " + place;
      console.log(str);
      return str;
    }
  }
  
  var myself = new Person('Rizky Husain','Indonesia');
  myself.greeting();