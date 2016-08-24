var a = 0
(1 until 1000).map(i => (i % 3, i % 5) match {
  case(0, _) => a = a+i
  case(_, 0) => a = a+i
  case _ => Nil
})
println(a)