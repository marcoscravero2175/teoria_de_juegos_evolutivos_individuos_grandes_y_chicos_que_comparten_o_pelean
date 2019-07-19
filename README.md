# Teoria de los Juegos Evolutivos. Machos fieles y atorrantes, hembras faciles y esquivas.

## Simulacion online

https://grandes-chicos-comparten-pelea.herokuapp.com/


## Resumen

En este trabajo se implementan vario de los juegos de la teoría evolutiva de los juegos desarrollada por Maynard Smith en su libro Evolución y Teoría de Juegos y popularizada principalmente por Richard Dawkins en el libro El Gen Egoísta: Las Bases Biológicas de Nuestra Conducta.  Esta teoría nos permite entender como pudo haber evolucionado la moral en los animales. Los juegos se programaron en python, javascript, html y se usó el framework “Mesa”,  desarrollado por Washington DC, George Mason University. https://www.researchgate.net/publication/328774079_Mesa_An_Agent-Based_Modeling_Framework

Primero empezamos con una población donde todos los individuos son exactamente iguales y existen solamente dos estrategias que pueden usar, compartir o pelear. Luego agregamos diferencias arbitrarias entre los individuos y estrategias condicionales, como pelear solo si mi oponente es más viejo o es el intruso. Después convertimos las diferencias arbitrarias en diferencias que influyen en la probabilidad de ganar una pelea y vimos que sucede si la mayoría de la población usa una estrategia condicional contradictoria, como pelear solo si mi oponente es más grande y fuerte. Por ultimo consideramos una población formada por individuos distintos pero cada clase de individuos tienen distinto conjunto de estrategia, por ejemplo una población formada por machos y hembras y las estrategias de las hembras pueden ser fáciles y esquivas y las estrategias de los machos pueden ser atorrantes o fieles.

En la implementación nos encontramos con una serie de problemas, por ejemplo el problema de la sobrepoblación, si los individuos más aptos tienen 2 o más descendientes el crecimiento es exponencial y en pocas generaciones nos quedamos sin recursos.  Analizamos el tema de la  distancia mínima a la que tienen que estar dos individuos para que surja un conflicto por algún recurso. Vemos cuales son los recursos intelectuales mínimos que suponemos que tienen los individuos simulados.

El informe consta de una introducción teórica (teoría evolutiva de los juegos, los problemas encontrados en la implementación, sobrepoblación, soluciones implementadas) y un análisis de los resultados obtenidos en las simulaciones realizadas.


## Introduccion



Los animales necesitan determinados recursos para vivir, por ejemplo agua, comida, refugio, etc. Si un ambiente es favorable un individuo tiene más descendientes que en un ambiente desfavorable. Tal vez el lector se preguntara si es verdad que un animal en un ambiente favorable tiene más crías que en un ambiente desfavorable, que evidencia empírica hay para esta afirmación. Maynad Smith en Evolución y Teoría de los juegos, libro  citado por todos los que escriben sobre teoría de los juegos evolutivo  dice "el valor de un recurso es el aumento en la aptitud darwiniana del individuo que obtiene el recurso, supongamos que los animales con un territorio en un el hábitat favorable tienen, en promedio, 5 crías, y los que se reproducen en el hábitat menos favorable tiene 3 crías, entonces V, el valor del recurso, sería igual a 5 - 3 = 2 ". 

Lo que escribe Maynard Smith no es estrictamente cierto por varias razones. En lugar, en nuestra especie observamos que las personas pobres y sin estudios tienen muchos más hijos que las personas con dinero y esto no significa que los pobres tengan mayor aptitud darwiniana que los ricos. Pero nuestra especie es un caso especial,  ninguna otra existe pudo construir un estado benefactor. 

Hay otra razón de porque lo que escribió Maynard Smith es falso. Un animal puede tener muchas más crías que otro,  por ejemplo, un individuo puede tener 20 crías y otro solo 3. El individuo que tiene 20 crías no necesariamente es más apto que el que tiene solo 3 si todas las crías del que tuvo 20 mueren antes del primer mes de vida, porque los padres no pueden alimentarlas a todas y no pueden decidir a qué cría dejar morir, mientras que los que tienen solo 3 crías se convierten en abuelo de varios nietos.

Pero volviendo al tema del ambiente favorable lo que si podemos decir es que un animal que vive en un ambiente favorable tiene más crías que llegan a la edad adulta y a su vez estas crías tienen crías, que un animal que vive en un ambiente desfavorable. Si fuese al revés, esto es si un animal en un ambiente desfavorable tuviera más crías y a su vez esas crías tuvieran más crías que un animal en un ambiente favorable, entonces el ambiente favorable no sería tal y el ambiente desfavorable en realidad sería un ambiente favorable. Y si la cantidad de crías fuese igual entonces el ambiente no sería un factor de selección y los organismos no evolucionarían o evolucionarían por otra razón. 

Ahora volvamos al tema de la relación entre cantidad de crías y valor de los recursos ¿Cuantas crías más tuvo el que comió una ración más de comida, el que comió un venado más, el que sufrió un poco de hambre? No es fácil asignarles valores numéricos a los recursos, ni convertir los puntos en cantidad de descendientes, pero las predicciones suele usar relaciones de orden, no números exactos. Mientras menos duro sea el ambiente y más riesgosas las peleas, más dispuestos van a estar los individuos de compartir la comida. En la simulación los individuos van sumando puntos con cada recurso que consiguen, cada recurso aporta una pequeña fracción al total de puntos. Cuando el individuo llega a una determinada edad, se reproduce asexualmente creando copias de sí mismo de acuerdo a la cantidad de puntos obtenidos y  luego, el individuo muere.

Las plantas no se dejan comer, producen sabores desagradables, los animales tampoco se dejan comer, las gacelas evolucionan para correr más rápido, haciéndoles hacen cada vez la vida más difícil a los leones. En este modelo no vamos a considerar  la carrera armamentística asimetría entre presas y depredadores, ni tampoco la evolución de la vista de los pájaros para ver a insectos que se camuflaba y mimetizaban cada vez mejor con el ambiente. Vamos a suponer que en cada posición del tablero,  el ambiente donde se desarrolla la simulación, hay recursos que los animales necesitan para vivir.

Hay recursos que se pueden compartir y hay recursos que no se pueden dividir, ni se pueden compartir. Hay situaciones en las cuales a un animal no le conviene compartir un recurso, por ejemplo si un ambiente favorable tiene para el animal 10 puntos, y un ambiente menos favorable tiene 8 puntos, a nadie le convendría compartir y tener  5 putos cuando puede irse a un ambiente desfavorable y tener 8 puntos. En los modelos que presentaremos supondremos que los recursos son divisibles y que a los animales les conviene tener la mitad antes que quedarse sin nada y buscar otro recurso de menor valor. 

Un conflicto se produce cuando dos individuos quieren el mismo recurso. Los conflictos se pueden resolver en forma pacífica, esto es, compartiendo el recurso, o puede escalar el conflicto, se produce una pelea que termina con uno de los dos contrincantes gravemente lesionado.   Las lesiones producidas en un combate entre dos animales son costosas, también es un costo, aunque menor, el tiempo perdido amenazando al contrincante, gruñendo o mostrándole los dientes.

En una guerra de desgaste solo el ganador obtiene el recurso pero ambos contrincantes pagan el mismo coste. Por ejemplo, si el coste está dado por el tiempo que duro la pelea, ambos perdieron el mismo tiempo. Si el coste está dado por lesiones recibidas, supongamos que un contrincante está dispuesto a pelear hasta que tenga el ojo en compota y el rival hasta las costillas rota. Empieza la pela, un contrincante tira un puño y le rompe el tabique nasal, como los contrincantes son físicamente iguales, el otro tira en puño y le rompe el tabique nasal al otro. Así hasta que llegan a los ojo en compota, momento en que uno de los contrincantes se retira y el otro gana. En este caso gana el animal que estaba dispuesto a pelear hasta tener una costilla rota y ambos animales pagan el costo de romperse el tabique nasal. 

En el juego de halcones y palomas el ganador obtiene recurso, pero a diferencia de la guerra de desgaste solo el perdedor paga el coste, el ganador no resulta lesionado. Si bien las peleas entre animales se parecen más a una guerra de desgaste asimétrica  que a un juego de halcones y palomas, para seguir el modelo de Maynad Smith  implemente el juego de halcones y palomas, solo el perdedor paga el costo y el ganador obtiene el recurso sin resultar lesionado.

¿Cuáles son las capacidades cognitivas o intelectuales mínimas que tienen que tener los individuos? ¿Es necesario que los animales puedan reconocer a los otros individualmente? ¿Es necesario que los animales tengan memoria, que pueda recordar las lucha pasadas? Sabemos que el altruismo puede evolucionar si un individuo puede reconocer a individuos altruistas y ayudar solo a los que reconoció como altruista, si un individuo altruista se tira a un rio para salvar 10 individuos el altruistas podría morir, pero el gen para altruismo podría evolucionar si salvo a 10 individuos. De igual manera la cooperación puede evolucionar si hay reconocimiento individual de los miembros de la población. En un dilema del prisionero repetido, la estrategia que empieza cooperando y después coopera si el contrincante coopero con migo en el pasado y desertar en caso contrario. El castigo hace posible la evolución de la cooperación en grupos de cierto tamaño. Si el coste de castigar es relativamente bajo —algo que puede garantizarse casi siempre que surge la práctica de castigar a aquellos que no castigan lo bastante—, se crea una máquina generadora de conformismo grupal de alcance y poder aparentemente ilimitado 

Estos dos casos, altruismo y cooperación, los modelos suponen reconocimiento individual y memoria, coopero si Juan copero con migo en el pasado, lo ayudo a Juan que se está ahogando si pertenece al conjunto de los que ayudan a personas que se ahogan. 

En el modelo que  implemente no hay reconocimiento, ni memoria.  Los individuos son anónimos, no saben, antes de comenzar la pelea si el oponente es violento o pacifico, y tampoco queda recuerdo en la memoria de combate con el individuo.

Por más de que los individuos tengan capacidades cognitivas superiores, memoria y reconocimiento individual, un modelo simple se podría aplicar a varias situaciones, como conflictos que surgen con alguien desconocido y que nunca más vas a volver a ver. En una pelea de transito con alguien desconocido existe una probabilidad muy baja de encontrarse de nuevo con el mismo individuo. Un estacionamiento no se puede compartir, pero en muchas otras situaciones donde se produce conflicto con personas desconocidas y con muy bajas probabilidad de volverse a encontrar.

¿Puedo tener un conflicto con alguien que este a 10km o en la otra punta del tablero? ¿‘A cuantos pasos tengo que estar de alguien para que surja un conflicto? Los modelos matemáticos se abstraen de la vecindad, todos los individuos de la población son vecinos de toso, en la simulaciones decimos a cuantos pasos tiene que estar un individuo para considerarse vecinos. ¿Cuál es distancia mínima en cual dos individuos se consideran vecinos que compiten por algún recurso? Considerar que todos los agentes que hay en el ambiente son vecinos entre sí puede dar resultados muy diferentes a lo que sucede en la realidad. Por ejemplo, anteriormente vimos que la estrategia del dilema del prisionero repetido, cooperar si el individuo coopero con migo en el pasado” necesita que los agentes se puedan reconocer individualmente. El éxito de la estrategia depende de lo que está haciendo la mayoría de la población, si la mayoría de la población está cooperando, desertar no es buena idea. Recíprocamente, si la mayoría de la población está desertando, cuando aparezca alguien de coopere todos se van a aprovechar del ingenuo que empieza cooperando.  Pero una diferencia importante entre las dos estrategias es que cooperar si el otro coopero en el pasado tiene muy buen desempeño cuando se enfrenta con copias de sí mismo. Si los descendientes de cooperar heredan la estrategia y  nacen uno cerca uno del otro, cuando se encuentran tienen muy buen desempeño y les va mucho mejor que a los descendientes de siempre desertar que se encuentran copias de siempre desertar. Esta propiedad de la estrategia hace que crezca mucho más rápido que siempre desertar y en pocos pasos cooperar si anteriormente coopero se hace mayoría en la población y cuando alcance la mayoría en la población se convierte en la mejor estrategia que puede adoptar un individuo en la población. En la simulación se puede configurar la vecindad. Una vecindad de todo el ambiente da igual resultado que modelos matemáticos en los que se abstraen de la vecindad.

La cantidad de hijos que un padre tiene depende de los recursos conseguidos y las lesiones sufridas. Los individuos viven una determinada edad se reproducen y luego mueren, por ejemplo pueden vivir 6 pasos de simulación  dejar 2 hijos. Los hijos son iguales que sus padres, son clones de sus padres ya que en el modelo la reproducción es asexual, heredan la misma forma de resolución de conflictos.  Si los padres resolvían los conflictos compartiendo, los hijos van a compartir, si los padres resolvían las disputas peleando los hijos van a resolver las disputas peleando. El final del juego habrá más individuos que compartan y más individuos violentos.

La explosión demográfica es un problema en nuestra especie y en la simulación. En la naturaleza las poblaciones de animales no crecen hasta quedarse sin recurso. ¿Cómo lo hacen? Si la mitad de la población, los más aptos, tienen 2 hijos el crecimiento es exponencial y en pocas generaciones se produce una sobrepoblación. En cambio si hago que los individuos más aptos tengan un solo hijo, y los menos aptos no tengan ningún hijo,  en cada generación se va reduciendo la población. Los biólogos propusieron varias explicaciones de porque son muy raras las explosiones demográficas en la naturaleza. Una explicación, por el bien de la especie,  es selección de grupo, los individuos se reúnen, hacen un censo y se decide, inconscientemente, cuantos descendientes se tendrá en la próxima generación. 

Hay otra explicación con más evidencia empírica. Tener un hijo tiene un coste y solo se obtiene una ganancia si el hijo  llega sano y salvo a la edad adulta y le dé nietos. En la población hay individuos que están genéticamente programados para tener 20 hijos, hay individuos que están programados para temes 10 y los hay que tiene solo 5 hijos independientemente de su aptitud. Si un individuos pone 20 huevos y no puede alimentarlos, mueren todos sus hijos y entonces deja menos descendía que alguien que solo puso 3 huevos, pudo alimentar a los 3 y todos llegaron sanos y salvo a la edad adulta. Esto da como resultado una regulación dinámica de la cantidad de hijos óptimos.  Por cuestiones de simplicidad para la simulación se implementó una política centralizada, como la explicación del censo, se cuanta la cantidad total de individuos de la población y en base a esto se decide cuantos hijos se tendrán en la próxima generación.
Los modelos simples pueden volverse gradualmente más complejos. Esperamos que medida que se vuelven más complejos se asemejen más al mundo real. 

Primero supondremos una población donde todos los individuos son exactamente iguales, clones. Luego, un gen mutado, diferencia a los individuos entre quienes resuelven los conflictos peleando y quienes resuelven los conflictos compartiendo, sigue sin haber diferencia física entre los individuos. 

Después agregaremos una diferencia arbitraria, por ejemplo el color de cabello o si tiene barba o no tiene barba, que no influyen en la fuerza física, ni en la capacidad de lucha e introduciremos estrategias condicionales, como pelear si mi oponente tiene el cabello más oscuro que el mío y compartir en caso contrario. 

Veremos qué pasa cuando los individuos se diferencian en atributo que influye en la fuerza o en  la capacidad de lucha, que pasa con individuos que luchan si mi contrincante es más fuerte y huyen si es alguien más débil.

Por ultimo realizaremos simulaciones en una población formada por machos y hembras, donde los machos tienen las estrategas fiel y atorrante y las hembras fáciles y esquivas.

Nota: Dawkins dice si una paloma se enfrenta a otra paloma nadie saldrá lesionado; se limitarán a asumir una postura, una frente a la otra, durante un largo tiempo hasta que una de ellas se canse o decida no molestarse más y, por lo tanto, ceda, Maynard Smith dice que el recurso se comparte de manera equitativa entre los dos participantes. Hablan de que  palomas solo exhiben, muestran amenazan, comparten, mientras que los halcones son más agresivos y escalan. La gente común cuando le explico el juego pienso que los halcones son más grandes físicamente que las palomas. Si bien el juego que implemento se conoce como el juego de  Halcones y Palomas yo voy a usar comparten y pelean. Más allá de las palabras, el juego tiene la misma tabla de pagos que es lo único que importa.


## Compartir o pelear en población donde todos los individuos son iguales


En el primer modelo que implementamos suponemos que todos los individuos son exactamente iguales, no se diferencian en nada, hasta que surge un conflicto. Unos resuelven los conflictos compartiendo y otros peleando.    No sabe qué estrategia va a usar el oponente hasta que empiece el combate. No puede haber estrategia del tipo altruista, si mi oponente es de los que comparten yo voy a compartir, porque no hay forma de saber qué hará el oponente. Tampoco puede haber estrategia de tipo colaborativa, si mi oponente compartió en el pasado voy a compartir, no hay discriminación individual, no sé si  tuve un conflicto anterior con el mismo oponente, ni se cómo se comportó en disputas anteriores. 

Como decimos, todo individuo de la población se clasifica en dos tipos, los que siguen una estrategia de pelear y los que comparten. Si alguien que usa la estrategia atar tiene un conflicto con alguien que usa la estrategia compartir, ésta se alejará rápidamente y así no resultará dañada. Si alguien que usa la estrategia atacar tiene un conflicto con otro que usa la estrategia atar, continuarán la lucha hasta que uno de ellos resulte muerto o gravemente herido. Si alguien que usa la estrategia compartir se enfrenta a otra que use la estrategia compartir nadie saldrá lesionado; el recurso se comparte de manera equitativa entre los dos participantes. Por el momento, asumiremos que no hay forma de que un individuo pueda saber, por adelantado, si un rival determinado es un halcón o una paloma. Sólo lo descubre al iniciarse la lucha, y no guarda memoria de pasadas luchas con otros individuos por las cuales guiarse.
Matriz de pagos

Dawkins dice que en los elefantes marinos, el premio por obtener una victoria puede estar cercano a obtener derechos casi monopolistas sobre un numeroso harén de hembras. El resultado final por el triunfo debe estar, en consecuencia, calificado bastante alto. No es de extrañar que las luchas sean crueles. El costo de perder el tiempo para un pájaro pequeño en un clima frío, por otra parte, puede ser gigantesco. Un gran paro, cuando se encuentra alimentando a sus polluelos necesita atrapar una presa cada treinta segundos por término medio. Sabemos demasiado poco en la actualidad, desgraciadamente, para asignar cifras realistas a los costos y beneficios de las diversas consecuencias que resultan de los diversos actos en la naturaleza.

Las estrategias son hereditarias. Los individuos que comparten tuvieron un padre que compartía y los individuos que pelean tuvieron un padre que peleaba. Una de las estrategias es compartir. Se comparte si el otro también quiere compartir,  si el otro no quiere compartir, quiere pelear por el recurso, el que quiere compartir le cede el recurso al violento. La otra estrategia pelear, pelea hasta conseguir el recurso y hasta quedar gravemente lesionado.  Si elijo pelear y el otro elije pelear se da una pelea y dado que somos iguales físicamente se tiene el 50% de probabilidades de ganar y 50% de probabilidades de terminar gravemente lesionado.  

Sabemos que pasa cuando se enfrenta alguien que comparte contra alguien que pelea, el que pelea se queda con el recurso. Es fácil darse cuenta que sucede en una población donde el valor del recurso es mayor que el costo de lesión.

Si el valor del recurso es mayor que el coste de las lesiones producida por la pela al cabo de un par de generaciones todos los individuos pelearan. 

Si todos los individuos de la población pelean, como son individuos  físicamente iguales la probabilidad de ganar y obtener el recurso V es del 50% y la probabilidad de perder y resultar con una lesión de C es del 50%, por lo tanto en promedio se obtienen (V-C)/2.
Si en la población todos comparten, en cada enfrentamiento obtienen la mitad del recurso y por lo tanto en promedio obtienen V/2. 

Como vimos, si en la población todos los individuos pelean obtienen en promedio (V-C)/2. Si el valor del recurso V es mayor que el costo de lesión C, un individuo que comparta no puede invadir la población porque alguien que siempre seda el recurso obtiene 0 y 0 es menor que (V-C)/2. Si el valor del recurso V es menor que el costo de lesión C entonces la población va a ser una mezcla de individuos que pelen e individuos que compartan.

Recíprocamente, si en la población todos comparten obtienen en promedio V/2. Si se agrega un individuo que pelea va a ganar todos los combates y en promedio va obtener V. Si el valor del recurso es mayor que el costo de lesión, en algunas generaciones todos los individuos van a pelear. Si el valor del recurso es menor que el costo de lesión la población resultado va a ser una mezcla de individuos que compartan y peleen.

En ambos casos, si el valor del recurso es menor que el costo de lesión, obtenemos que el porcentaje de la población que va a compartir va a ser V/C.

E(compartir, estrategia mixta) = E(pelear, estrategia mixta)
P * E(H,H) + (1-P) * E(H, D) = P * E(D, H) + (1-P) * E(E, E)
(1/2) * (V-C) * P + V * (1-P) = (1/2) * V * (1-P)
C * P = V
V = 5;  C = 10; P  = 0.50

Veremos qué pasa en la simulación. ¿Al final de los juegos hay más individuos que resuelven sus conflictos a los golpes o deciden compartir?  ¿Qué pasa si en una población donde todos comparten se agrega un violento? ¿Puede invadir la población? ¿Qué pasa con una población donde todos son violentos y se agrega uno que comparte? 

Simulación: compartir o pelear en población donde todos los individuos son iguales

En la población todos los individuos son físicamente iguales, tienen la misma fuerza, el mismo  tamaño y  la probabilidad de que individuo cualquiera gane una pelea es del 0.50. Además los individuos no ven ninguna diferencia entre ellos, esto es, no puede haber  estrategias condicionales del tipo “si mi oponente es un individuo  grande (pequeño) entonces pelea (comparte)”.

El primer sub-caso son de poblaciones donde el valor del recurso es mayor que el coste de lesión, el segundo sub-caso el valor del recurso es menor que el coste de lesión

a- Valor del recurso mayor que costo de lesión

En la primera simulación todos los individuos de la población usan la estrategia de compartir, el valor del recurso es de 10 puntos,  el costo de lesión es de 5 puntos, la vecindad es de 30 pasos y veremos qué pasa cuando agregamos un individuo que use la estrategia pelear.

El estado inicial de la población es el siguiente:

 Luego de 5 generaciones todos los individuos pelean
 
Los porcentajes iniciales son:

Porcentaje luego de 62 generaciones

 Luego de 160 generaciones los porcentajes son:
 
 Como es lógico, si el valor del recurso es mayor que el costo de pelea todos los individuos van a pelear.
 
La evolución del sistema fue la siguiente:
En el estado final todos pelean

b- Valor recurso menor que el costo de lesión

Ahora, en la población en la que todos pelean, cambiamos el valor del recurso de 10 puntos a 5 puntos, el coste de lesión de 5 puntos a 10 puntos y agregamos un individuo que compartes.

Luego de 5 generaciones tenemos el siguiente estado

Los porcentajes luego de 5 generaciones son:

Dado que el valor del recurso, (V), es de 5 puntos y el costo de lesión, (P),  es de 10 puntos el porcentaje tendría que ser, (V/C), 0.50, muy próximo a lo que se observa en la simulación.

Los porcentajes encontrados simulando están cerca de los que se deducen matemáticamente.

La evolución del sistema fue la siguiente:

 El estado final




## Estrategias condicionales usando diferencias arbitrarias entre los individuos

En la vida real no somos clones, no somos todos iguales, además de la diferencia en resolución de conflictos, hay diferencias arbitrarias, como el color de pelo, joven-viejo, intruso-local que no influyen en el resultado de una pelea y hay diferencias entre los individuos, como fuerza física o tamaño que si influye en resultado de un conflicto. Primero vamos a considerar diferencias en atributos no influyen en el resultado de un conflicto, como tener barba verde,  ser viejo-joven, residente-intruso, cabello oscuro, piel clara. Luego vamos a considerar diferencias que si influyen en el resultado de una pelea, como ser más grande y más fuerte.

Supongamos una población con una diferencia arbitraria, puede ser individuos jóvenes o individuos viejos, individuos que son intrusos e individuos locales, además suponemos que cada individuo sabe si él es local o intruso, viejo o joven, sabe que su oponente es local o es el intruso, viejo o joven, pero no puede saber si su oponente va a estar dispuesto a compartir el recurso o pelear. 

En un punto anterior se explicó el altruismo, un individuo se arroja al rio y muere pero logra salvar a 10 individuos altruistas, con individuos que pueden reconocer a individuos altruistas y tienen una estrategia condicional del tipo “si el que se está ahogando es un individuo altruista tirarse al rio e intentar salvarlo. En este caso no podemos tener una estrategia del tipo “comparto solo con los individuos que comparten” porque no hay indicios de si comporte o pelea, solo sé que el que se está ahogando tiene tal color de cabello, no sé si es de los que ante un conflicto pelea o comparte. 

En un punto anterior también se explicó que puede surgir la cooperación en un dilema del prisionero repetido, cuando hay reconocimiento individual, memoria de encuentros anteriores y una estrategia condicional del tipo “compartir si en oportunidades anteriores el individuo compartió y desertar en caso contrario”. En el juego que estamos considerando no hay reconocimiento individual, ni memoria de conflictos pasados. Esto se puede deber a que no tengan memoria, o a que sea muy raro que dos individuos se vuelvan a encontrar en el futuro, como pueden ser un conflicto entre dos desconocidos en una gran ciudad.

Como los individuos son diferentes en algún aspecto podemos ahora agregar estrategias condicionales. Además de las estrategias simples,   siempre compartir, siempre pelear, vamos a   agregar una tercera estrategia, una estrategia condicional,  “pelear solo si mi contrincante tiene el cabello más oscuro que mi color de cabello y compartir en caso contrario”. ¿Qué sucederá en este caso? ¿Qué estrategia me conviene a mí adoptar para ganar más puntos? ¿Si vas a roma has le de los romanos, si todos están usando la estrategia condicional me conviene hacer lo que todos hacen?

Sabemos que si el recurso vale más que el costo de una lesión conviene pelear y que si el costo de una lesión es mayor de que valor del recurso lo que conviene hacer depende de lo que está haciendo la población,  va a haber un porcentaje de la población que comparta y otro que pelee, el porcentaje depende del valor del recurso y del costo de lesión, a mayor costo de lesión menor cantidad de individuos van pelear. Ahora veremos qué pasa con estrategia condicional que depende de una diferencia arbitraria que hay entre los individuos.
Dawkins dice Supongamos que todos los individuos representen «el residente gana, el intruso huye». Ello significaría que ganarían la mitad de sus batallas y perderían el resto. Nunca resultarían heridos y nunca perderían el tiempo, ya que todas las disputas quedarían inmediatamente zanjadas por una convención arbitraria. Consideremos ahora a un nuevo mutante rebelde. Supongamos que él juega la estrategia del halcón, siempre atacando y nunca retirándose. Ganará cuando su adversario sea un intruso. Cuando su adversario sea un residente, correrá un grave riesgo de resultar herido. Como promedio obtendrá un resultado menor que los individuos que aceptan las reglas arbitrarias de la EEE. Una mera asimetría arbitraria y aparentemente irrelevante pueda dar origen a una EEE, ya que puede ser utilizada para arreglar rápidamente las contiendas. Pongamos un ejemplo: se dará a menudo el caso de que un contendiente llegue primero al lugar de la contienda que el otro. Denominémoslos «residente» e «intruso», respectivamente. Lo que dice Dawkins no es estrictamente.  

Como será una simulación si tengo una población de individuos grandes o residentes e individuos chicos o intrusos que siguen la siguiente estrategia condicional “si eres residente pelea, en caso contrario comparte o huye” y agrego un individuo grande o residente que sigue la estrategia siempre pelear, este individuo va a tener el mismo desempeño que si sigue la estrategia condicional y al cabo de cualquier número de generaciones la población va tener el mismo porcentaje de individuos que agregue. Si agrego a la población un 10% de individuos grandes que siempre pelean, al cabo de mil generaciones voy a seguir teniendo un 10%  individuos grandes que siempre pelean.
Los individuos grandes tienen hijos grandes, los individuos que siempre pelean tienen hijos que siempre pelean, los individuos grandes y que siempre pelean tiene hijos grandes y que siempre pelean. Los individuos que tienen un mejor desempeño tienen mayor cantidad de hijos.  Los individuos grandes que siempre pelean tienen igual desempeño que los individuos que siguen la estrategia si eres grande pelea, en caso contrario comparte, por lo tanto tienen igual cantidad de descendiente y las proporciones se mantienen, no invade la población, ni desaparecen.

Lo mismo pasa si agrego individuos chicos que siempre comparten a una población donde todos los individuos usan la estrategia condicional pelear solo con individuos chicos. No hay individuos más chicos que los individuos chicos, los individuos chicos que siempre comparten son indistinguibles en la población de individuos que usan estrategia condicional de sentido común
Se puede ver en la simulación que si todos los individuos están usando la estrategia condicional “si mi oponente tiene el cabello más oscuro que el mío entonces pelear, en caso contrario compartir” y el valor del recurso es menor que el costo de una lesión, ninguna otra estrategia puede invadir esa población.

Simulación: estrategias condicionales usando diferencias arbitrarias entre los individuos

En la población los individuos son distintos pero la diferencia no influye en el resultado de un combate, esto es, la probabilidad de que gane un individuo grande es de 0.50 y la probabilidad de que gane un individuo chico es de 0.50. Ahora, a diferencia del caso anterior,   los individuos se pueden distinguir, un individuo sabe a qué clase pertenece y a que clase pertenece su oponente. Esto da como resultado que pueda haber individuos que usen estrategias condicionales del tipo” sí mi oponente es un individuo es grande (pequeño) entonces pelea (comparte)”

Las diferencias que hay entre los individuos son arbitrarias, esto es, las diferencias entre los individuos no influyen en el resultado de una pelea. Por lo tanto las probabilidades de que gane el individuo llamado grande es 0.50 y la probabilidad de que gane el individuo llamado chico es de 0.50.

Primero veremos que sucede cuando en la población hay igual cantidad de individuos que usan la estrategia “pelean solo si su contrincante es mayor” e “individuos que usan la estrategia pelear solo si su contrincante es menor”. Luego veremos lo que pasa cuando hay más individuos que siguen la estrategia “pelear solo si su contrincante es mayor”. Por ultimo consideramos población donde la mayoría de los individuos siguen la estrategia “pelear solo si su contrincante es menor”

a- La mitad de la población usa una de las estrategias condicionales y la otra mitad usa la otra estrategia condicional

En la población hay igual cantidad de individuos con estrategia condicional de sentido común e individuo con estrategia condicional paradójico, esto es igual cantidad de individuo que solo pelean si el contrincante es de menor tamaño e individuo que solo pelean si su contrincante es de mayor tamaño entonces luego de varias generaciones todos los individuos de la población van a seguir  una estrategia condicional de sentido común o todos los individuos de la población van a seguir una estrategia condicional paradójico, con una probabilidad de 0.50 todos los individuos van a seguir la estrategia condicional de sentido común y con una probabilidad de 0.50 todos los individuos van a seguir una estrategia condicional paradójico. 

El valor del recurso es de 5 puntos, el coste de lesión es de 10 puntos, 10 individuos chicos que pelean si su oponente es mayor y comparten en caso contrario, 10 individuos grandes que pelean si su oponente es menor y la probabilidades de que gane un individuo chico es igual a la probabilidad de que gane el individuo grande, igual a 0.50.

Los porcentajes iniciales son:

Luego de varias generaciones encontramos que todos los individuos de la población usan estrategia condicional paradoja.

La evolución del sistema fue la siguiente:

Los porcentajes luego de 5 generaciones son:

En otra simulación, luego de varias generaciones, encontramos que todos los individuos de la población usan estrategia condicional de sentido común.

Evolución del sistema:

 Estado final luego de 40 generaciones:
 
b- Más de la mitad de los individuos usa una de las estrategias condicionales

La probabilidad de que gane el más grande sigue siendo de 0.50 y la probabilidad de que gane el más chico del 0.50 pero ahora en la población hay una mayor cantidad de individuos que siguen una estrategia paradójico que individuos que siguen una estrategia condicional de sentido común. Como vamos a comprobar, luego de varias generaciones todos los individuos de la población van a usar la estrategia condicional paradójica.

Supongamos que tenemos la siguiente población:

-	10 individuos chicos que pelean si su adversario es grande y comparten si es grande.

-	8 individuos grandes que pelean si su adversario es chico y comparten si es grande.

El costo de lesión es de 10 puntos, el valor del recurso es de 5 puntos,  tienen la misma probabilidad de ganar un individuo chico que uno grande y hay más individuos chicos que pelean si su adversario es más grande que individuos grandes que pelean si su adversario es menor. ¿A qué evoluciona esta población?

Luego de 10 generaciones todos los individuos son chicos y pelean si su oponente es más grande:

Evolución del sistema:

c- Más de la mitad de los individuos usa la otra estrategia condicional 

Ahora vemos lo que pasa cuando empezamos con una población donde la mayoría de la población sigue una estrategia de sentido común. 
Ahora repitamos las simulaciones viendo lo que pasa cuando el costo de lesión es menor que el valor del recurso. Recordemos la población:

-	8 individuos chicos que pelean si su adversario es  grande y comparten en caso contrario.

-	10 individuos grandes que pelean si su adversario es chico y comparten en caso contrario.

¿Qué sucede en esta población? El costo de lesión es de 5 puntos, el valor del recurso es de 10 puntos, tienen la misma probabilidad de ganar un individuo chico que uno grande y hay más individuos grandes que pelean si su adversario es más chico.

Luego de 15 generaciones todos los individuos van a ser grandes y van a pelear si su oponente es más chico

Evolución del sistema:

Una población donde todos sus individuos usan una estrategia condicional arbitraria no puede ser invadida por individuos que usen otra estrategia condicional arbitraria.



## Diferencias entre individuos en aspectos que influyen en el resultado de una pelea

Ahora consideremos una población donde los individuos son distintos, pero en aspectos que influyen en el resultado de una pelea, por ejemplo la fuerza y el tamaño. En la población hay individuos grandes y fuertes e individuos pequeños y débiles. Al igual que en los casos anteriores, los individuos no saben cómo reaccionara el oponente, si estará dispuesto a compartir o tendrá ganas de pelear. Solo sé que el animal es más grande, o más chico, no sé si está dispuesto a atacarme o podemos compartir el recurso. 

Un ejemplo de asimetría puede ser el tamaño, hay individuos grandes e individuos chicos, otro ejemplo puede ser el sexo, hay individuos que son machos y otros que son hembras. Para simplificar asumamos que la asimetría puede tener solo dos valores, por ejemplo grande o chico, no hay individuos más o menos grandes, ni individuos que pesen 62 kg y otros que pesen 75kg, solo podemos clasificar a los individuos en grandes o chicos. En una pelea entre dos individuos grandes existe la misma probabilidad de que gane uno o de que gane el otro, igualmente una pelea entre individuos chicos tenemos el 50% de probabilidad de que gane uno o de que gane el otro. Pero cuando se enfrenta un individuo grande contra un individuo chico la probabilidad de que gane el más grande es un parámetro del modelo. Si queremos que el más grande siempre gane ponemos un porcentaje de 100. Si en peleas entre grandes y chicos el 80% de las veces gana el más grande ajustamos el parámetro del modelo a 80.

En una población asimétrica del tipo que estamos considerando pueden existir cuatro estrategias. Las dos estrategias que teníamos en la población simétrica, Siempre pelear, siempre  compartir, y dos estrategias condicionales, una de sentido común, pelear si mi oponente es de menor tamaño y compartir y caso contrario, y una estrategia condicional paradójica, pelear si mi oponente es más grande y compartir en caso contrario.

Fácilmente uno se puede dar cuenta que los costes de lesión son mayores que el valor del recurso una buena estrategia es “pelear con los que son más chicos que vos y compartir el recurso en caso contrario”. En una población donde todos golpean a los más débiles no puede ser invadida por ninguna de las otras dos estrategias, siempre pelear, ni por siempre compartir.

¿Qué pasa una población donde todos los individuos usan estrategia condicional paradójica, esto es, pelean si su oponente es más grande y comparten en caso contrario? ¿Puede ser invadido por alguna de las otras alternativas, por ejemplo por, siempre pelear, siempre compartir, o pelear solo si mi oponente es menor? Si el costo de lesión es superior al valor del recurso, la probabilidad de que el mayor gane es del 0.80 y todos siguen la estrategia paradójica, un individuo que siga la estrategia de sentido común, “pelear solo si el oponente es menor y compartir en caso contrario” no podrá invadir esta población, está en peor situación que alguien que siga una estrategia paradójica. Se pelearía con todos, y con un costo de lesión de más de 8 veces el valor del recurso, una probabilidad de ganar del 80% no compensa. 

Si los machos son más fuertes y grandes que las hembras, el 80% de las peleas entre machos y hembras las gana un macho, una estrategia condicional paradójica del tipo si sos hembra y tu contrincante es un macho atacar,  y si sos macho y tu contendiente es una hembra huir podría ser una estrategia evolutivamente estable. Cualquiera que hiciera algo distinto estaría en desventaja, las estrategias siempre huir, siempre pelear, están en desventaja contra la estrategia condicional paradójica que estaría usando la mayoría de la población. Aunque no es fácil decir cómo podría llegar una población a que todos sus miembros adopten una estrategia condicional paradójica, no hay etapas intermedias que sean evolutivamente estables.

Simulación: diferencias entre individuos en aspectos que influyen en el resultado de una pelea

Realizaremos simulaciones con casos donde los individuos son físicamente distintos, uno es más grande,  más fuerte que el otro,  y por lo tanto, la probabilidad de que el individuo más grande gane  es mayor que la probabilidad de que gane el individuo más chico gane. Los individuos pueden ver el tamaño del oponente y pueden usar estrategias condicionales “si mi oponente es un individuo es grande (pequeño) entonces peleo (comparto) en caso contrario comparto (peleo)”.

Hay individuos que comparten y han individuos que pelean, hay individuos chicos y han individuos grandes, el resultado de una pelea depende del tamaño del individuo. ¿Qué sucederá en esta población?

 a- La mitad de la población usa una estrategia condicional la otra mitad de la población usa la otra estrategia condicional pero la probabilidades de ganar  una pelea es mayor siendo grande que pequeño
 
Supongamos que el 90% de las veces que pelean un individuo grande contra un individuo chico gana el individuo más grande. Costo de lesión 10 puntos, valor del recurso 5 puntos, 10 individuos chicos que solo pelean si su oponente es mayor y 10 individuos grandes que pelean si su oponente es más chico y comparten en caso contrario.

10 individuos chicos  usan una estrategia condicional paradójica.

10 individuos  usan estrategia condicional de sentido común.

El individuo más grande gana 9 de cada 10 peleas. 

Luego de 15 generaciones obtenemos los siguientes porcentajes

Evolución de la población:

 b- La mitad de la población usa una estrategia condicional la otra mitad de la población usa la otra estrategia condicional pero la probabilidades de ganar siendo grande es mayor que siendo pequeño
 
Supongamos que el costo de lesión es de 10, el valor del recurso es de 5 y que el 10% de las veces en que pelea un individuo grande contra un individuo chico la gana el individuo grande. Tenemos una población con 5 individuos granes que siempre pelean, 5 individuos chicos que siempre pelean y agregamos 2 individuos que solo pelean si su contrincantes es menor, en caso contrario comparten.
Ahora, hacemos que el costo de lesión es de 5, el valor del recurso es de 10 

10 individuos chicos  usan una estrategia condicional paradójica.

10 individuos  usan estrategia condicional de sentido común.

Si solo el 10% de las veces gana el más grande luego de 5 generaciones obtengo lo siguiente

 La evolución de la población fue la siguiente
 
 c- La mitad de la población usa una estrategia condicional la otra mitad de la población usa la otra estrategia condicional pero la probabilidades de ganar siendo grande es menor que siendo pequeño
 
Supongamos que en la población todos pelean solo si el contrincante es más grande y comparten cuando el oponente es más chico. 

Supongamos que soy un individuo grande que el 80% de las peleas entre un individuo grande y uno chico la gana el individuo grande, que el coste de una lesión es de 9 puntos, el valor del recurso es de 1 punto.  ¿Siendo yo un individuo grande y estando en una población de paradojicos, que me conviene hacer? ¿Compartir o pelear?

Tenemos una población con 10 individuos paradójicos, esto es, individuos chicos que pelean si su oponente es más grande y comparten en caso contrario. Ahora agregamos un individuo grande que pelea con individuos más chicos y comparten en caso contrario y vemos que sucede en la población, si puede o no puede invadir la población.

Tenemos una población de 10 individuos chicos que usan una estrategia paradójica, esto es pelea con los oponentes que son más grandes y comparte en caso contrario y 8 individuos que usan estrategia condicional de sentido común. ¿A que evoluciona esta población?
10 individuos chicos  usan una estrategia condicional paradójica.

 8 individuos  usan estrategia condicional de sentido común.
 
El individuo más grande gana 8 de cada 10 peleas. 

 Luego de 10 generaciones se obtienen los siguientes porcentajes
 Y la evolución fue la siguiente
 
 Como se observa individuos que usen estrategia de sentido común no puede invadir una población con individuos que usen estrategia paradójica.



## Juegos con estrategias evolutivas inestables

Como vimos anteriormente, con tema de la sobrepoblación, tener 5 hijos no siempre es evolutivamente mejor que tener 2 hijos. Tener un hijo tiene un costo y se obtiene recompensa cuando el descendiente llega sano y salvo a la edad adulta y  puede dar nietos. Una carrera armamentística produjo diferencias entre los sexos.  El ovulo es más grande y aporta nutrientes, los espermatozoides son mucho más chicos y tienen movilidad. Hay dimorfismo sexual, los machos son más grandes porque compiten por las hembras, las crías se desarrollan dentro del cuerpo de la madre.

En la reproducción sexual los costos de tener un hijo lo puede pagar uno solo de los progenitores o se pueden compartir entre los dos.  No están sobre este planeta las especies donde los machos se marcharon, dejando sola a las hembras, y como venganza las hembras también se marchaban dejando morir a la cría. Pero las hembras tienen una carta en su mano, pueden seleccionar machos con buenos genes o machos que realicen aportes, como construir un nido, antes de copular. 

Una hembra puede exigir que el macho le construya un nido antes de copular. La estrategia que se adopte un individuo depende de lo que está haciendo el resto de la población. Un hornero construye un nido porque todas las hembras exigen lo mismo para copular.

Como puede elegir una hembra machos con buenos genes. ¿Cómo puede saber si no le están mintiendo, si solamente aparenta que es el macho más fuerte, pero en realidad los músculos son falsos? Los pavo real macho tienen colas llamativas que les dificulta caminar son atractivos para las hembras, porque son atractivas para las hembras o porque pueden mostrar que aun con una dificultad llegaron a la edad adulta. La explicación que hoy en día se acepta es que las señales son honestas porque son costosas, el principio de la desventaja. 
En la primer parte se consideraron dos tipos distintos de individuos, individuos grandes y chicos. Ambos individuos tenían las mismas estrategias disponibles. Los individuos grandes podían compartir o pelear, y los individuos chicos también podían compartir y pelear. Ahora consideremos dos tipos de individuos, pero cada individuo tiene distintas estrategias.  

Supongamos que los tipos de individuos son machos y hembras. Las estrategias de los machos son fieles o atorrantes y las hembras pueden ser fáciles y esquivas. Supongamos que la ventaja evolutiva por tener una  cría le da 15 puntos a cada uno de los padres, supongamos que el coste para tener una criar una cría con éxito es de 20 puntos, este coste se puede repartir entre los padres o lo pude pagar solo la hembra dependiendo del tipo de estrategia, supongamos que en un cortejo se pierden 3 puntos.

-En un encuentro de macho atorrante con una hembra fácil, le da al macho 15 puntos y a la hembra -5 puntos.

-Un encuentro entre un macho fiel y una hembra esquiva, el macho gana 2 puntos, esto es 15 de la cría -10 de la crianza compartida, -3 del cortejo. La hembra también obtiene el mismo puntaje.

-Un encuentro entre un macho atorrante y una hembra esquiva cada uno obtiene 0 puntos, no tienen ninguna cría, no hay cortejo, ni hay costo de crianza.

-Un encuentro entre un macho fiel y una hembra fácil, el macho consigue 5 puntos y la hembra también consigue 5 puntos.

Si se analiza el juego parecería que hay un equilibrio estable. En la primera edición del Gen Egoísta, Richard Dawkins pensaba que este juego tenía un equilibro  Como se dio cuenta luego un matemático el equilibro es inestable, el juego oscila, una vez que se alcanza el equilibrio, si se produce una pequeña modificación en los porcentajes, lejos de autorregularse y volver al equilibrio, el desequilibrio se potencia hasta alcanzar un equilibrio distinto.

Supongamos una población donde todas las hembras son fáciles y todos los machos fieles, si se introduce un macho atorrante este, a diferencia del macho fiel, no paga el coste de la crianza, por lo tanto va a obtener mejores puntajes que un macho fiel y el número de machos atorrantes aumenta.

A medida que los machos atorrantes aumentan, las hembras fáciles empiezan a tener menos ventaja que las hembras esquivas. Cuando la mayoría de los machos son atorrantes, las hembras esquivas obtienen mejor resultado que las hembras fáciles y por lo tanto su número aumenta.

Cuando se llega a unan situación donde todas las hembras son esquivas y los machos atorrantes, un macho fiel puede invadir la población, obtiene mejor desempeño que un macho atorrante.

Si todas las hembras son esquivas y los machos son files, una hembra fácil puede invadir la población y sacar ventaja de que todos los machos son fieles. En este punto estamos en la misma situación que cuando se empezó el ciclo, una población donde las hembras son fáciles y los machos son fieles.

Análisis de simulaciones realizadas

Se puede realizar la simulación en cualquier navegador web online:

https://grandes-chicos-comparten-pelea.herokuapp.com/

El código fuente escrito en python usando el framework mesa:

https://github.com/marcoscravero2175/teoria_de_juegos_evolutivos_individuos_grandes_y_chicos_que_comparten_o_pelean

Machos fieles y atorrantes, hembras fáciles y esquivas

Se implementó el juego evolutivo descripto por Dawkins en el Gen Egoísta.

Simulación online:

https://machos-hembras.herokuapp.com/

Código fuente en python usando el framework mesa:

https://github.com/marcoscravero2175/teoria_de_juegos_evolutivos_machos_fieles_y_atorrantes_hembras_faciles_y_esquivas

## Conclusión

Si población está formada por individuos iguales y el costo de lesión es mayor que el valor del recurso los porcentajes encontrados en la simulación oscilan alrededor del valor teórico. Esto se debe a que cuando el porcentaje es menor que el teórico, por ejemplo, supongamos que los que comparten tienen un porcentaje menor que el teóricamente esperado,  los que comparten van a ser los más aptos, porque van a conseguir más puntos, van a duplicar su porcentaje en la población y en la siguiente generación los que van a ser más aptos van a ser los otros, los que pelean, van a duplicar su población, así hasta que hay sobrepoblación y eliminamos aleatoriamente individuos de la población manteniendo los porcentajes a los que había llegado la simulación.

Vimos que en todas las simulaciones donde hay un 20% más de individuos que siguen estrategia condicional paradójico, esto es pelear solo con individuos que son más grandes, el costo de lesión es 8 veces mayor que el valor del recurso, la probabilidad de que el mayor gane es de 0.80, esta población no pudo ser invadido por individuos que siguen estrategia condicional de sentido común, esto es pelear solo contra individuos que son más chicos.

Como pudimos una población con 10 individuos chicos que pelean solo si su oponente es más grande, 8 individuos grandes que pelean solo si su oponente es más chico, los individuos grandes ganan el 80% de las peleas, el costo de lesión 5 puntos y valor del recurso 10 puntos evoluciona a una población donde todos los individuos son chicos y pelean solo si su oponente es más grande.


* **Richard Dawkins, El Gen Egoista.**
* **Richard Dawkins, El Relojero Ciego.**
* **Richard Dawkins, Escalando el Monte Improbable.**
* **Richard Dawkins, El Rio del Eden.**
* **Daniel Dennett, La Peligrosa Idea de Darwin.**
* **Daniel Dennett, La Evolucion de La Libertad.**
* **Steven Pinker, La Tabla Rasa.**
* **Steven Pinker, El Instinto del Lenguaje.**
* **John Maynard Smith, Evolucion y Teoria de los Juegos.**
* **John Maynard Smith, Animal Signals.**






 
