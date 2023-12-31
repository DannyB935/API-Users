--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2
-- Dumped by pg_dump version 15.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: usuario; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.usuario (
    id character varying(50) NOT NULL,
    name character varying(50) NOT NULL,
    lastname character varying(50) NOT NULL,
    username character varying(20) NOT NULL,
    password character varying(256) NOT NULL,
    age integer NOT NULL,
    photo character varying(256),
    deleted boolean DEFAULT false NOT NULL,
    rol integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.usuario OWNER TO postgres;

--
-- Data for Name: usuario; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.usuario (id, name, lastname, username, password, age, photo, deleted, rol) FROM stdin;
06637acd-99fc-4280-a70c-1b291958eb3f	Danny	Ruiz	Danny	a79938ab5392c8024dff98a44cf776f4cbbb47be9ff78e4997a4920ec262b320	23		f	1
ebd43f83-122a-4d93-b183-ec5c4a208bf8	Juan	Nada	Prueba	550c9f7fa060a860f3c6e72d0c88d3ff072d8da4dc9483a8fb97ce5ed06cd5cf	18		f	0
bf097f3a-06c4-4d83-ba01-1b44f2e5b566	Elena	Sánchez	elena_sanchez87	7540db5cd679cc5a5a2574a25786028c1bb588f70f94eda7d35c92ec8d08eae7	18		f	0
3099711d-298e-4f37-9e86-ab1d7c3316df	Lucas	Rodríguez	lrodriguez_23	86a3caf5301479747b7f652947170d667bd472a33e016913c641bf98c8532d1f	18		f	0
30424b07-3d21-4dc9-9814-637c246cb48d	Sofia	Patel	sofia.patel_56	e76c3f3e44b75bacb786ffd03dc00609c441bc3dc684ce79c66e77ae442cdfb5	18		f	0
\.


--
-- Name: usuario usuario_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

