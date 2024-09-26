class Person (val name: String, val age: Int) {
    fun displayInfo() {
        println("$name is $age years old")
    }
}

fun main() {
    val person = Person("Olzhas", 25)

    person.displayInfo()
}
