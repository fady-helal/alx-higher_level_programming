#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;

  for (let i = 0; i < list.length / 2; i++) {
    const rmp = list[i];
    list[i] = list[len];
    list[len] = rmp;
    len--;
  }
  return list;
};
