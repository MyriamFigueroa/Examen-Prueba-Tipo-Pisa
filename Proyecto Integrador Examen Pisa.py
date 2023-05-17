def main():
    puntaje_comprension = 0
    puntaje_matematicas = 0
    puntaje_ciencias = 0
    print(" === BIENVENIDO A TU EXAMEN DE PRUEBA TIPO PISA ===")
    nombre = input('Introduce tu nombre: ')
    edad = input('Introduce tu edad: ')
    grado = input('Introduce tu grado escolar: ')
    fecha = input('Introduce la fecha de realización (dd/mm/aaaa): ')
    print('\nAhora empezarás con la sección de Comprensión lectora. \n'
          'Esta sección se compone de 10 preguntas de opción multiple.\n'
          'Responde de acuerdo a lo que tu consideres correcto. \n'
          'Responde con letras en minúscula (a, b, c, d)\n'
          '¡Éxito! :)\n')
    print('==== COMPRENSIÓN LECTORA ====\n')
    print('Los siguientes ejercicios están basados en \n '
          'el contenido de las lecturas. Después de leerlas,\n'
          'selecciona la mejor respuesta para cada ejercicio\n'
          'y oscurece el espacio correspondiente en la hoja\n'
          'de respuestas. Contesta todos los ejercicios\n'
          'basándote en lo que las lecturas afirman\n'
          'o sugieren')
    print('\nLa rama vibró, cediendo al peso de una paloma cuando\n'
          'se posó sobre ella. La paloma, asustada, respiraba fuerte,\n'
          'miraba de lado a lado sin saber a dónde dirigirse.\n'
          '—¿Y por qué tan asustada? —preguntó una voz\n'
          'que no podía identificar en aquella oscuridad tan densa\n'
          'que le rodeaba.\n'
          '—¿Quién anda ahí? ¿Quién habla? —preguntó la paloma.\n'
          'La rama volvió a vibrar. Esta vez por el movimiento\n'
          'de una ardilla que disfrutaba de un buen sueño reparador.\n'
          '—¿Le tienes miedo a la oscuridad? —indagó la\n'
          'ardilla, abriéndose camino hacia la atemorizada paloma.\n'
          '—Sí, mucho. No veo nada. Se hizo de noche y ahora\n'
          'no encuentro el camino de regreso.\n'
          '—¡Ah!, pero, si dejaras de intentar verlo todo,\n'
          'la noche no sería tan oscura.\n'
          'Ahora, aparte de miedo, la paloma comenzó \n'
          'a sentir una gran confusión.\n'
          '—No entiendo lo que dices. Tengo que ver para\n'
          'saber a dónde voy. La ardilla encontró un rayo de\n'
          'luz de luna que se colaba entre las hojas del árbol\n'
          'y se colocó debajo para que la paloma pudiera verla.\n'
          '—La noche se vuelve más oscura si te empeñas\n'
          'en ver; andar o volar de noche es como ir con los\n'
          'ojos cerrados.\n'
          '—¡Pero es que si vuelo con los ojos cerrados\n'
          'puedo chocar!\n'
          'A la paloma le parecía una locura lo que estaba\n'
          'diciendo la ardilla.\n'
          '—¡Puedo no ver un árbol y PUM, me reviento!\n'
          '—De día ves. Ves mucho. Ves demasiado. Ves nada\n'
          'más y te olvidas del resto de los sentidos. Pero de noche...\n'
          'de noche, apagas los ojos y enciendes los otros sentidos y\n'
          'el mundo se transforma, se vuelve diferente. A ver, cierra\n'
          'los ojos.'
          'La paloma ni chistó, así que la ardilla insistió:\n'
          '“Dale, cierra los ojos”.\n'
          '—Ok, ok, voy a cerrarlos. ¡Ya! Cerrados.\n'
          '—¿Qué sientes? —preguntó la ardilla.\n'
          '—¡Miedo! —contestó la paloma.\n'
          '—¿Y qué más? ¿Sientes el viento?\n'
          '—Sí, lo siento frío y con olor a humedad.\n'
          '—¿Y qué más sientes?\n'
          'En esta ocasión, la paloma se concentró y apretó\n'
          'fuertemente los párpados. Quizás, si lo pensaba bien,\n'
          'la ardilla, dentro de su locura, tenía razón.\n'
          '—El viento viene del este. Lo sé porque sabe\n'
          'a sal y porque huele al infinito que nos baña con\n'
          'su blanca espuma.\n'
          'Antes de que la ardilla pudiera decir algo más,\n'
          'la paloma continuó —¡y... las oigo! Oigo a mis\n'
          'compañeras llamándome... ¡por allá!'
          'La rama crujió de nuevo con el movimiento\n'
          'del viento bajo las alas de la paloma, mientras esta\n'
          'alzaba vuelo guiada por los arrullos de sus compañeras.\n'
          'Entonces la ardilla, satisfecha de su obra, se echó a\n'
          'dormir nuevamente en aquella noche oscura impregnada\n'
          'de la fría brisa marina\n')
    pregunta1 = input('Según la lectura, la palabra “densa” (línea 5) significa: \n'
                      'a) espesa\n'
                      'b) compacta\n'
                      'c) tenebrosa\n'
                      'd) misteriosa\n')
    if pregunta1.lower() == 'a':
          puntaje_comprension += 1
          print('¡Respuesta correcta! :)\n')
    else:
        print('Respuesta incorrecta :(\n')
    pregunta2 = input('Según la lectura, la frase “infinito que nos baña con su blanca espuma” (líneas 50-51) se refiere al:\n'
                      'a) viento\n'
                      'b) bosque\n'
                      'c) río\n'
                      'd) mar\n')
    if pregunta2.lower() == 'd':
        puntaje_comprension += 1
        print('¡Respuesta correcta! :)\n')
    else:
        print('Respuesta incorrecta :(\n')
    pregunta3 = input('Al principio de la lectura, se INFIERE que la paloma estaba asustada porque\n'
                      'a) no veía a la ardilla\n'
                      'b) la rama del árbol vibraba\n'
                      'c) estaba perdida\n'
                      'd) la ardilla apareció de repente\n')
    if pregunta3.lower() == 'c':
        puntaje_comprension += 1
        print('¡Respuesta correcta! :)\n')
    else:
        print('Respuesta incorrecta :(\n')
    pregunta4 = input('De la lectura se INFIERE que la paloma vivía\n'
                      'a) cerca del mar\n'
                      'b) a la orilla de un río\n'
                      'c) en un árbol cercano\n'
                      'd) en la cima de un monte\n')
    if pregunta4.lower() == 'a':
        puntaje_comprension += 1
        print('¡Respuesta correcta! :)\n')
    else:
        print('Respuesta incorrecta :(\n')
    pregunta5 = input('De la lectura se puede concluir que la paloma\n'
                      'a) esperó hasta el amanecer en la rama\n'
                      'b) regresó con las demás palomas\n'
                      'c) se quedó a dormir con la ardilla\n'
                      'd) confundió la dirección del viento\n')
    if pregunta5.lower() == 'b':
        puntaje_comprension += 1
        print('¡Respuesta correcta! :)\n')
    else:
        print('Respuesta incorrecta :(\n')
    print(" === LECTURA 2 ===")
    print('\nEl canguro es un mamífero marsupial oriundo de\n'
          'Australia, Nueva Zelanda y Tasmania. En Australia,\n'
          'por ejemplo, existen tres tipos de canguros: el rojo, el\n'
          'gris oriental y el gris occidental. El canguro rojo, el más\n'
          'grande de todos, se reconoce fácilmente por el tono rojizo\n'
          'de su pelaje y por el tono gris claro de la parte inferior\n'
          'del vientre. Tiene la cabeza más pequeña que las otras\n'
          'especies, pero las orejas más largas y puntiagudas. Suele\n'
          'vivir en zonas áridas, pues no tolera las zonas húmedas.\n'
          'El canguro gris oriental ocupa el segundo lugar por\n'
          'su tamaño. Tiene el cuerpo más musculoso y, erguido,\n'
          'puede llegar a medir 2 metros. Su pelaje es de un gris\n'
          'casi uniforme, un poco más oscuro en el rostro y más\n'
          'claro en el vientre. Se adapta bien a cualquier hábitat:\n'
          'vive en bosques secos y en regiones costeras.\n'
          'El canguro gris occidental es el más pequeño de\n'
          'tamaño. Tiene el hocico cubierto de un pelaje muy fino.\n'
          'El color del resto del cuerpo varía del marrón grisáceo\n'
          'al marrón oscuro con reflejos rojizos. En el abdomen,\n'
          'el pecho y el cuello, el pelo es más claro, y más oscuro en\n'
          'la punta de la cola y extremidades. Habita en pastizales,\n'
          'matorrales y diversos tipos de bosques abiertos.\n'
          'Estos tres tipos comparten varias características.\n'
          'Las hembras tienen una bolsa en el abdomen, el\n'
          'marsupio, en el que terminan la gestación de sus crías\n'
          'y las amamantan. Por otro lado, estos tres tipos de\n'
          'canguros tienen la cola y las patas traseras muy fuertes,\n'
          'lo que les sirve para apoyarse, mantener el equilibrio,\n'
          'desplazarse y mantenerse de pie. Además, saltan y se\n'
          'mueven a una velocidad de entre 20 a 25 km/h, aunque\n'
          'cuando necesitan correr, pueden hacerlo a 70 km/h.\n'
          'Por último, como herbívoros, se alimentan de hierbas,\n'
          'hojas, flores, helechos, musgos o frutas. Salen a buscar el\n'
          'alimento en grupo para protegerse de los depredadores,\n'
          'especialmente del zorro rojo y del dingo, que es un tipo\n'
          'de lobo australiano.\n')
    pregunta6 = input('En la lectura, la palabra “erguido” (línea 11) significa:\n'
                      'a) alerta\n'
                      'b) estirado\n'
                      'c) firme\n'
                      'd) derecho\n')
    if pregunta6.lower() == 'd':
        puntaje_comprension += 1
        print('¡Respuesta correcta! :)\n')
    else:
        print('Respuesta incorrecta :(\n')
    pregunta7 = input('En la lectura, la palabra “hocico” (línea 17) se refiere a la\n'
                      'a) frente y orejas\n'
                      'b) boca y nariz\n'
                      'c) boca y dientes\n'
                      'd) nariz y ojos\n')
    if pregunta7.lower() == 'b':
        puntaje_comprension += 1
        print('¡Respuesta correcta! :)\n')
    else:
        print('Respuesta incorrecta :(\n')
    pregunta8 = input('Según la lectura, los canguros son mamíferos marsupiales por:\n'
                      'a) el proceso de gestación de estos animales\n'
                      'b) la fortaleza y firmeza de las patas y la cola\n'
                      'c) las diferencias en el pelaje de cada especie\n'
                      'd) el tipo de salto que realiza para desplazarse\n')
    if pregunta8.lower() == 'a':
        puntaje_comprension += 1
        print('¡Respuesta correcta! :)\n')
    else:
        print('Respuesta incorrecta :(\n')
    pregunta9 = input('De la lectura se INFIERE que el canguro rojo\n'
                      'a) puede llegar a medir más de dos metros\n'
                      'b) vive en las zonas secas de Australia\n'
                      'c) se desplaza mediante saltos cortos\n'
                      'd) se reconoce por el color de su pelaje\n')
    if pregunta9.lower() == 'a':
        puntaje_comprension += 1
        print('¡Respuesta correcta! :)\n')
    else:
        print('Respuesta incorrecta :(\n')
    pregunta10 = input('En la lectura predomina la\n'
                       'a) narración\n'
                       'b) descripción\n'
                       'c) exposición\n'
                       'd) argumentación\n')
    if pregunta10.lower() == 'b':
        puntaje_comprension += 1
        print('¡Respuesta correcta! :)\n')
    else:
        print('Respuesta incorrecta :(\n')

    print('=== HAS LLEGADO AL FINAL DE LA SECCIÓN DE ESPAÑOL ===\n')

    print("\n=== MATEMÁTICAS ===")
    print('\nAhora empezarás con la sección de Matemáticas. \n'
          'Esta sección se compone de 10 preguntas de opción multiple.\n'
          'Responde de acuerdo a lo que tu consideres correcto. \n'
          'Responde con letras en minúscula (a, b, c, d)\n'
          '¡Éxito! :)\n')

    print("En un concierto de rock se reservó para el público un terreno rectangular con unas \n"
          "dimensiones de 100 m por 50 m. Se vendieron todas las entradas y el terreno se llenó\n"
          "de aficionados, todos de pie.")
    pregunta11 = input("¿Cuál de las siguientes constituye la mejor estimación del número total de asistentes al concierto? \n"
          "a) 2.000\n"
          "b) 5.000\n"
          "c) 20.000\n"
          "d) 50.000\n"
          "e) 100.000 \n")
    if pregunta11.lower() == 'c':
        puntaje_matematicas += 1
        print('¡Respuesta correcta! :)\n')
    else:
        print('Respuesta incorrecta :(\n')
    pregunta12 = input("La subida al Monte Fuji sólo está abierta al público desde el 1 de julio hasta el 27 de \n "
                       "agosto de cada año. Alrededor de unas 200.000 personas suben al Monte Fuji durante \n "
                       "este periodo de tiempo. \n"
          "a) 340\n"
          "b) 710\n"
          "c) 3.400\n"
          "d) 7.100\n"
          "e) 7.400 \n")
    if pregunta12.lower() == "c":
        puntaje_matematicas += 1
        print('¡Respuesta correcta! :)\n')
    else:
        print('Respuesta incorrecta :(\n')
    pregunta13 = input("¿Cuál de las siguientes expresiones es equivalente a 11^2 · 11^4? \n"
                       "a) 116\n"
                       "b) 118\n"
                       "c) 1216\n"
                       "d) 1218\n")
    if pregunta13.lower() == "a":
        puntaje_matematicas += 1
        print('¡Respuesta correcta! :)\n')
    else:
        print('Respuesta incorrecta :(\n')
    pregunta14 = input("Halla la factorización prima de 72\n"
                       "a) 2^2 x 18\n"
                       "b) 2^3 x 3^2\n"
                       "c) 8 × 3^2\n"
                       "d) 8 × 9\n")
    if pregunta14.lower() == "b":
        puntaje_matematicas += 1
        print('¡Respuesta correcta! :)\n')
    else:
        print('Respuesta incorrecta :(\n')
    pregunta15 = input("¿Cuál de los siguientes números es divisible por 2 y por 3? \n"
                       "a) 8\n"
                       "b) 15\n"
                       "c) 24\n"
                       "d) 35\n")
    if pregunta15.lower() == "c":
        puntaje_matematicas += 1
        print('¡Respuesta correcta! :)\n')
    else:
        print('Respuesta incorrecta :(\n')
    pregunta16 = input("Halla el valor de 3(6 + 1 – 9)\n"
                       "a) –10\n"
                       "b) –6\n"
                       "c) 6\n"
                       "d) 10\n")
    if pregunta16.lower() == "b":
        puntaje_matematicas += 1
        print('¡Respuesta correcta! :)\n')
    else:
        print('Respuesta incorrecta :(\n')
    pregunta17 = input("¿Cuántas veces cabe 2/8 en 14? \n"
                       "a) 14\n"
                       "b) 24\n"
                       "c) 28\n"
                       "d) 56\n")
    if pregunta17.lower() == "d":
        puntaje_matematicas += 1
        print('¡Respuesta correcta! :)\n')
    else:
        print('Respuesta incorrecta :(\n')
    pregunta18 = input("Ramón perdió 40 de los 4000 puntos que había acumulado en un juego de video. \n"
                       "¿Cuál fue el porcentaje de puntos que perdió Ramón?\n"
                       "a) 0.01 %\n"
                       "b) 0.1 %\n"
                       "c) 1 %\n"
                       "d) 10 %\n")
    if pregunta18.lower() == "c":
        puntaje_matematicas += 1
        print('¡Respuesta correcta! :)\n')
    else:
        print('Respuesta incorrecta :(\n')
    pregunta19 = input("Silvia compra perfumes para venderlos en su tienda. Cada pedido de perfumes se compone \n"
                       "de tres cajas grandes. En cada una de estas hay dos \n"
                       "cajas medianas. En cada caja mediana hay cuatro \n"
                       "cajas pequeñas. Si ella hace 3 pedidos de perfumes, \n"
                       "¿cuál es el número total de cajas que recibirá?\n"
                       "a) 24\n"
                       "b) 33\n"
                       "c) 72\n"
                       "d) 99\n")
    if pregunta19.lower() == "d":
        puntaje_matematicas += 1
        print('¡Respuesta correcta! :)\n')
    else:
        print('Respuesta incorrecta :(\n')
    pregunta20 = input("Sarai recorrió hoy cinco kilómetros más que el triple \n"
                       "de lo que recorrió ayer. Si x representa la distancia \n"
                       "recorrida ayer, ¿cuál de las siguientes expresiones \n"
                       "representa los kilómetros recorridos hoy?\n"
                       "a) 3x + 5\n"
                       "b) 3(x + 5)\n"
                       "c) x^3 + 5\n"
                       "d) (x + 5)^3\n")
    if pregunta20.lower() == "a":
        puntaje_matematicas += 1
        print('¡Respuesta correcta! :)\n')
    else:
        print('Respuesta incorrecta :(\n')

    print('=== HAS LLEGADO AL FINAL DE LA SECCIÓN DE MATEMÁTICAS ===\n')

    print('\n=== CIENCIAS ===')
    print('\nAhora empezarás con la sección de Ciencias. \n'
          'Esta sección se compone de 10 preguntas de opción multiple.\n'
          'Responde de acuerdo a lo que tu consideres correcto. \n'
          'Responde con letras en minúscula (a, b, c, d)\n'
          '¡Éxito! :)\n')

    pregunta21 = input('¿Qué contienen los cloroplastos de las células vegetales?\n'
                      'a) Clorofila\n'
                      'b) Agua\n'
                      'c) Sábila\n')
    if pregunta21.lower() == 'a':
        print('¡Respuesta correcta! :)\n')
    else:
        print('Respuesta incorrecta :(\n')
    pregunta22 = input('¿Qué significan las siglas ADN?\n'
                       'a) Ácido deoxinucleico\n'
                       'b) Ácido desorribonucleico\n'
                       'c) Ácido desocirribonucleico\n')
    if pregunta22.lower() == 'c':
        print('¡Respuesta correcta! :)\n')
    else:
        print('Respuesta incorrecta :(\n')
    pregunta23 = input('Todos los organismos del reino Animalia son:\n'
                       'a) Multicelulares y autótrofos\n'
                       'b) Multicelulares y heterótrofos\n'
                       'c) Unicelulares y heterótrofos\n')
    if pregunta23.lower() == 'b':
        print('¡Respuesta correcta! :)\n')
    else:
        print('Respuesta incorrecta :(\n')
    pregunta24 = input('¿Cómo se denomina a un grupo de crías de perro?\n'
                       'a) Camada\n'
                       'b) Manada\n'
                       'c) Piara\n')
    if pregunta24.lower() == 'a':
        print('¡Respuesta correcta! :)\n')
    else:
        print('Respuesta incorrecta :(\n')
    pregunta25 = input('¿Qué es un cardumen?\n'
                       'a) Una especie de planta\n'
                       'b) Un banco de peces\n'
                       'c) Una parte del abdomen de los insectos\n')
    if pregunta25.lower() == 'b':
        print('¡Respuesta correcta! :)\n')
    else:
        print('Respuesta incorrecta :(\n')
    pregunta26 = input('¿Qué bioma o paisaje bioclimático se caracteriza por tener una capa de permafrost?\n'
                       'a) Taiga\n'
                       'b) Tundra\n'
                       'c) Savanna\n')
    if pregunta26.lower() == 'b':
        print('¡Respuesta correcta! :)\n')
    else:
        print('Respuesta incorrecta :(\n')
    pregunta27 = input('La salamandra es un animal de sangre caliente\n'
                        'a) Verdadero\n'
                        'b) Falso\n')
    if pregunta27.lower() == 'b':
        print('¡Respuesta correcta! :)\n')
    else:
        print('Respuesta incorrecta :(\n')
    pregunta28 = input('HISTORIA DE LA VACUNACIÓN \n'
                       'Mary Montagú era una mujer muy guapa. En 1715 sobrevivió a un ataque de \n'
                       'viruela, pero quedó cubierta de cicatrices. En 1717, cuando vivía en Turquía, \n'
                       'observó un método llamado inoculación que se usaba frecuentemente allí. Este \n'
                       'tratamiento consistía en infectar con un tipo de viruela debilitada, mediante un \n'
                       'arañazo en la piel, a una persona joven y sana, que luego enfermaba, pero en la \n'
                       'mayoría de los casos sólo con una forma suave de la enfermedad. \n'
                       'Mary Montagú estaba tan convencida de la seguridad de esas inoculaciones que \n'
                       'permitió que se inocularan a su hijo y a su hija. \n'
                       'En 1796, Edward Jenner usó inoculaciones de una enfermedad próxima, la \n'
                       'viruela de las vacas, para producir anticuerpos frente a la viruela. En comparación \n'
                       'con la inoculación de la viruela, este tratamiento tenía menos efectos secundarios \n'
                       'y las personas tratadas no infectaban a otras. A este tratamiento se le conoce \n'
                       'con el nombre de vacunación.\n'
                       '¿Frente a qué tipo de enfermedades se puede vacunar a la gente?\n'
                       'a) Enfermedades hereditarias como la hemofilia\n'
                       'b) Enfermedades causadas por virus, como la polio\n'
                       'c) Enfermedades causadas por un mal funcionamiento del cuerpo, como la diabetes\n'
                       'd) Cualquier tipo de enfermedad que no tenga cura\n')
    if pregunta28.lower() == 'b':
        print('¡Respuesta correcta! :)\n')
    else:
        print('Respuesta incorrecta :(\n')
    pregunta29 = input("Si los animales o las personas padecen una enfermedad infecciosa bacteriana y luego \n"
                       "se recuperan, el tipo de bacteria causante de la enfermedad, en general, no vuelve a \n"
                       "infectarlos. ¿Cuál es la razón de este hecho?\n"
                       "a) El cuerpo ha matado todas las bacterias que pueden producir la misma enfermedad \n"
                       "b) El cuerpo ha fabricado anticuerpos que matan este tipo de bacterias antes de que \n"
                       "se multipliquen.\n"
                       "c) Los glóbulos rojos matan todas las bacterias que pueden producir la misma enfermedad \n"
                       "d) Los glóbulos rojos capturan y eliminan del cuerpo este tipo de bacterias\n")
    if pregunta29.lower() == 'b':
        print('¡Respuesta correcta! :)\n')
    else:
        print('Respuesta incorrecta :(\n')
    pregunta30 = input("Las bacterias que viven en nuestra boca provocan caries dental. La caries ha sido un\n"
                       "problema desde el año 1700, cuando el azúcar se hizo accesible, gracias al desarrollo \n"
                       "de la industria de la caña de azúcar.\n"
                       "Hoy en día sabemos mucho sobre la caries. Por ejemplo:\n"
                       "• Las bacterias que provocan la caries se alimentan de azúcar\n"
                       "• El azúcar se transforma en ácido \n"
                       "• El ácido daña la superficie de los dientes\n"
                       "• El cepillado de los dientes ayuda a prevenir la caries.\n"
                       "¿Cuál es el papel de las bacterias en la aparición de la caries dental?\n"
                       "a) Las bacterias producen esmalte \n"
                       "b) Las bacterias producen azúcar \n"
                       "c) Las bacterias producen minerales \n"
                       "d) Las bacterias producen ácido \n")
    if pregunta30.lower() == 'd':
        print('¡Respuesta correcta! :)\n')
    else:
        print('Respuesta incorrecta :(\n')

    print('=== HAS LLEGADO AL FINAL DE LA SECCIÓN DE CIENCIAS ===\n')
    print('\n === ¡FELICIDADES! HAS CONCLUIDO CON LA PRUEBA ===')

    print("\n","tu puntaje en la sección de español fue de:", puntaje_comprension)
    print("\n","tu puntaje en la sección de matemáticas fue de:", puntaje_matematicas)
    print("\n","tu puntaje en la sección de ciencias fue de:", puntaje_ciencias)
    print('\n','tu puntaje general fue de:', ((puntaje_comprension+puntaje_matematicas+puntaje_ciencias)*100)/30)

    if puntaje_comprension < 7:
        print('Te falta reforzar el área de español.')
    if puntaje_matematicas < 7:
        print('Te falta reforzar el área de matemáticas.')
    if puntaje_ciencias < 7:
        print('Te falta reforzar el área de ciencias.')



if __name__ == '__main__':
    main()