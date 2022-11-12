-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 25-10-2022 a las 03:31:27
-- Versión del servidor: 10.4.22-MariaDB
-- Versión de PHP: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `rh3`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `area`
--

CREATE TABLE `area` (
  `idArea` int(11) NOT NULL,
  `descripcion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `area`
--

INSERT INTO `area` (`idArea`, `descripcion`) VALUES
(1, 'mecanico'),
(2, 'maestro'),
(3, 'trabajos pasados');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carrera`
--

CREATE TABLE `carrera` (
  `idCarrera` int(11) NOT NULL,
  `descripcion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `carrera`
--

INSERT INTO `carrera` (`idCarrera`, `descripcion`) VALUES
(1, 'ingeniero en sistemas'),
(2, 'maestro en bilogia'),
(3, 'tecnologias de la cumunicacion');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `escolaridad`
--

CREATE TABLE `escolaridad` (
  `idEscolaridad` int(11) NOT NULL,
  `descripcion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `escolaridad`
--

INSERT INTO `escolaridad` (`idEscolaridad`, `descripcion`) VALUES
(1, 'primaria'),
(2, 'secundaria'),
(3, 'preparatoria');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estadocivil`
--

CREATE TABLE `estadocivil` (
  `idEstadoCivil` int(11) NOT NULL,
  `descripcion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `estadocivil`
--

INSERT INTO `estadocivil` (`idEstadoCivil`, `descripcion`) VALUES
(1, 'casado'),
(2, 'soltero');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `gradoavance`
--

CREATE TABLE `gradoavance` (
  `idGradoAvance` int(11) NOT NULL,
  `descripcion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `gradoavance`
--

INSERT INTO `gradoavance` (`idGradoAvance`, `descripcion`) VALUES
(1, 'estudiando'),
(2, 'terminado'),
(3, 'por salir');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `habilidad`
--

CREATE TABLE `habilidad` (
  `idHabilidad` int(11) NOT NULL,
  `descripcion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `habilidad`
--

INSERT INTO `habilidad` (`idHabilidad`, `descripcion`) VALUES
(1, 'no especificada'),
(2, 'muy sociable'),
(3, 'memoria ');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `idioma`
--

CREATE TABLE `idioma` (
  `idIdioma` int(11) NOT NULL,
  `descripcion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `idioma`
--

INSERT INTO `idioma` (`idIdioma`, `descripcion`) VALUES
(1, 'no especificada'),
(2, 'ingles'),
(3, 'español');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `puesto`
--

CREATE TABLE `puesto` (
  `idPuesto` int(11) NOT NULL,
  `codPuesto` varchar(15) NOT NULL,
  `idArea` int(11) NOT NULL,
  `nomPuesto` varchar(50) NOT NULL,
  `puestoJefeSup` varchar(50) NOT NULL,
  `jornada` varchar(70) NOT NULL,
  `remunMensual` int(11) NOT NULL,
  `prestaciones` varchar(70) NOT NULL,
  `descripcionGeneral` varchar(250) NOT NULL,
  `funciones` varchar(250) NOT NULL,
  `edad` varchar(50) NOT NULL,
  `sexo` varchar(15) NOT NULL,
  `idEstadoCivil` int(11) NOT NULL,
  `idEscolaridad` int(11) NOT NULL,
  `idGradoAvance` int(11) NOT NULL,
  `idCarrera` int(11) NOT NULL,
  `experiencia` varchar(70) NOT NULL,
  `conocimientos` varchar(70) NOT NULL,
  `manejoEquipo` varchar(70) NOT NULL,
  `reqFisicos` varchar(70) NOT NULL,
  `reqPsicologicos` varchar(70) NOT NULL,
  `responsabilidades` varchar(70) NOT NULL,
  `condicionesTrabajo` varchar(70) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `puesto`
--

INSERT INTO `puesto` (`idPuesto`, `codPuesto`, `idArea`, `nomPuesto`, `puestoJefeSup`, `jornada`, `remunMensual`, `prestaciones`, `descripcionGeneral`, `funciones`, `edad`, `sexo`, `idEstadoCivil`, `idEscolaridad`, `idGradoAvance`, `idCarrera`, `experiencia`, `conocimientos`, `manejoEquipo`, `reqFisicos`, `reqPsicologicos`, `responsabilidades`, `condicionesTrabajo`) VALUES
(1, 'V009', 5, 'SUPERVISOR DE TIENDA ', 'SUPERVISOR', 'LUNES A VIERNES', 5000, 'DE LEY', 'VENTAS AL PÚBLICO', 'VENDER', '18 A 45 AÑOS', 'Hombre', 1, 3, 2, 2, '2 AÑOS', 'VENTAS', 'DE COMPUTO', 'AGUDEZA VISUAL', 'MEMORIA A CORTO Y LARGO PLAZO', 'INVENTARIO', 'AGRADABLES'),
(3, 'v0008', 3, 'OBRERO', 'SUPERVISOR', 'LUNES A VIERNES', 5000, 'DE LEY', 'maquilar', 'trabajar', '18 A 45 AÑOS', 'Indistinto', 1, 2, 2, 1, '2 AÑOS', 'VENTAS', 'DE COMPUTO', 'AGUDEZA VISUAL', 'MEMORIA A CORTO Y LARGO PLAZO', 'INVENTARIO', 'AGRADABLES'),
(4, 'v010', 6, 'PROGRAMADOR', 'LIDER DE PROYECTO', 'LUNES A VIERNES 8:30am 4:30am SABADOS 9:00am  A 2:00am', 10000, 'DE LEY', 'ELABORACION DE SISTEMAS COMPUTACIONALES', 'PROGRAMAR, ANALISIS DE SISTEMAS', '18 a 70 años', 'Indistinto', 1, 3, 3, 1, '2 AÑOS', 'PROGRAMACION EN LENGUAJES JAVA, PYTHO, MANEJO DE BASES DE DATOS ', 'DE COMPUTO', 'NO NECESARIOS', 'NO NECESARIOS', 'NO ESPECIFICADAS', 'AGRADABLES'),
(5, 'p001', 5, 'JEFE DE MERCADOTECNIA', 'GERENTE', 'LUNES A VIERNES 8:30am 4:30am SABADOS 9:00am  A 2:00am', 6500, 'DE LEY', 'COORDINAR A PERSONAL DE MERCADOTECNIA', 'CORDINACIÓN', '25 A 50', 'Indistinto', 1, 3, 4, 13, '2 AÑOS', 'VENTAS', 'DE COMPUTO', 'NO NECESARIOS', 'MEMORIA A CORTO Y LARGO PLAZO', 'NO ESPECIFICADAS', 'AGRADABLES'),
(19, '56665', 3, 'obrero 2', 'ma', 'lubes a viernes', 4556, 'si', 'obrero de trbajo', 'trabajar', '30', 'Hombre', 1, 2, 2, 1, '40 años', 'varios', 'pesado', 'fuerza', 'estable', 'varias', 'muchas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `puesto_has_habilidad`
--

CREATE TABLE `puesto_has_habilidad` (
  `idPuesto` int(11) NOT NULL,
  `idHabilidad` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `puesto_has_habilidad`
--

INSERT INTO `puesto_has_habilidad` (`idPuesto`, `idHabilidad`) VALUES
(19, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `puesto_has_idioma`
--

CREATE TABLE `puesto_has_idioma` (
  `idPuesto` int(11) NOT NULL,
  `idIdioma` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `puesto_has_idioma`
--

INSERT INTO `puesto_has_idioma` (`idPuesto`, `idIdioma`) VALUES
(19, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `requisicion`
--

CREATE TABLE `requisicion` (
  `idRequisicion` int(11) NOT NULL,
  `folio` varchar(25) NOT NULL,
  `fechaElab` date NOT NULL,
  `fechaRecluta` date NOT NULL,
  `fechaInicVac` date NOT NULL,
  `motivoRequisicion` varchar(30) NOT NULL,
  `motivoEspecifique` varchar(70) NOT NULL,
  `tipoVacante` varchar(15) NOT NULL,
  `nomSolicita` varchar(70) NOT NULL,
  `nomAutoriza` varchar(70) NOT NULL,
  `nomRevisa` varchar(70) NOT NULL,
  `autorizada` tinyint(1) NOT NULL,
  `idPuesto` int(11) NOT NULL,
  `idArea` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `requisicion`
--

INSERT INTO `requisicion` (`idRequisicion`, `folio`, `fechaElab`, `fechaRecluta`, `fechaInicVac`, `motivoRequisicion`, `motivoEspecifique`, `tipoVacante`, `nomSolicita`, `nomAutoriza`, `nomRevisa`, `autorizada`, `idPuesto`, `idArea`) VALUES
(10, '345456', '2022-10-19', '2022-10-27', '2022-10-25', 'Baja', '', 'permanente', 'raul', '', '', 1, 4, 2),
(12, '4455', '2022-10-26', '2022-10-29', '2022-10-19', 'Nueva Creación', '', 'temporal', 'carlos', 'anya', 'pedro', 1, 19, 2);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `area`
--
ALTER TABLE `area`
  ADD PRIMARY KEY (`idArea`);

--
-- Indices de la tabla `carrera`
--
ALTER TABLE `carrera`
  ADD PRIMARY KEY (`idCarrera`);

--
-- Indices de la tabla `escolaridad`
--
ALTER TABLE `escolaridad`
  ADD PRIMARY KEY (`idEscolaridad`);

--
-- Indices de la tabla `estadocivil`
--
ALTER TABLE `estadocivil`
  ADD PRIMARY KEY (`idEstadoCivil`);

--
-- Indices de la tabla `gradoavance`
--
ALTER TABLE `gradoavance`
  ADD PRIMARY KEY (`idGradoAvance`);

--
-- Indices de la tabla `habilidad`
--
ALTER TABLE `habilidad`
  ADD PRIMARY KEY (`idHabilidad`);

--
-- Indices de la tabla `idioma`
--
ALTER TABLE `idioma`
  ADD PRIMARY KEY (`idIdioma`);

--
-- Indices de la tabla `puesto`
--
ALTER TABLE `puesto`
  ADD PRIMARY KEY (`idPuesto`),
  ADD KEY `idEscolaridad` (`idEscolaridad`),
  ADD KEY `idEstadoCivil` (`idEstadoCivil`),
  ADD KEY `idGradoAvance` (`idGradoAvance`),
  ADD KEY `idCarrera` (`idCarrera`),
  ADD KEY `area` (`idArea`);

--
-- Indices de la tabla `puesto_has_habilidad`
--
ALTER TABLE `puesto_has_habilidad`
  ADD PRIMARY KEY (`idPuesto`,`idHabilidad`) USING BTREE,
  ADD KEY `idHabilidad` (`idHabilidad`);

--
-- Indices de la tabla `puesto_has_idioma`
--
ALTER TABLE `puesto_has_idioma`
  ADD PRIMARY KEY (`idPuesto`,`idIdioma`) USING BTREE,
  ADD KEY `idIdioma` (`idIdioma`);

--
-- Indices de la tabla `requisicion`
--
ALTER TABLE `requisicion`
  ADD PRIMARY KEY (`idRequisicion`),
  ADD KEY `idPuesto` (`idPuesto`),
  ADD KEY `idArea` (`idArea`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `area`
--
ALTER TABLE `area`
  MODIFY `idArea` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `carrera`
--
ALTER TABLE `carrera`
  MODIFY `idCarrera` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `escolaridad`
--
ALTER TABLE `escolaridad`
  MODIFY `idEscolaridad` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `estadocivil`
--
ALTER TABLE `estadocivil`
  MODIFY `idEstadoCivil` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `gradoavance`
--
ALTER TABLE `gradoavance`
  MODIFY `idGradoAvance` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `habilidad`
--
ALTER TABLE `habilidad`
  MODIFY `idHabilidad` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `idioma`
--
ALTER TABLE `idioma`
  MODIFY `idIdioma` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `puesto`
--
ALTER TABLE `puesto`
  MODIFY `idPuesto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT de la tabla `requisicion`
--
ALTER TABLE `requisicion`
  MODIFY `idRequisicion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
