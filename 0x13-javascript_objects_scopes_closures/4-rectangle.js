#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let r = '';
      for (let j = 0; j < this.width; j++) {
        r = r + 'X';
      }
      console.log(r);
    }
  }

  rotate () {
    this.width = this.height;
    this.height = this.width;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
