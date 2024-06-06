class Person {
  constructor(name, next = null) {
    this.name = name;
    this.next = next;
  }
}

class LinkedList {
  constructor(name) {
    this.head = new Person(name, null);
  }

  // Adding a person to linked list.
  //
  push(name) {
    let person = new Person(name);
    if (this.tail) {
      const tail_person = this.tail;
      tail_person.next = person;
      this.tail = person;
      return;
    }
    this.head.next = person;
    this.tail = person;
  }

  // Searching in a linked list.
  search(name) {
    let person = this.head;

    while (true) {
      if (person.name === name) {
        return person;
      }
      if (person.next === null) {
        return "Not found";
      }
      person = person.next;
    }
  }
}

// let list = new LinkedList("James");
