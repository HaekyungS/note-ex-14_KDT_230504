function exampleOne(a) {
  if (typeof a === 'number') {
    if (a - Math.floor(a) !== 0) {
      throw new Error('정수를 입력해야 합니다.')
    }
  } else {
    throw new Error('정수를 입력해야 합니다.')
  }
}

// 위 코드를 파이썬으로 작성하기.