toc.dat                                                                                             0000600 0004000 0002000 00000003530 14530517231 0014441 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        PGDMP   *                
    {            users    16.0    16.0     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false         �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false         �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false         �           1262    16629    users    DATABASE     y   CREATE DATABASE users WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Mexico.1252';
    DROP DATABASE users;
                postgres    false         �            1259    16630    usuario    TABLE     �  CREATE TABLE public.usuario (
    id character varying(50) NOT NULL,
    name character varying(50) NOT NULL,
    lastname character varying(50) NOT NULL,
    username character varying(20) NOT NULL,
    password character varying(50) NOT NULL,
    age integer NOT NULL,
    photo character varying(256),
    deleted boolean DEFAULT false NOT NULL,
    rol integer DEFAULT 0 NOT NULL
);
    DROP TABLE public.usuario;
       public         heap    postgres    false         �          0    16630    usuario 
   TABLE DATA           c   COPY public.usuario (id, name, lastname, username, password, age, photo, deleted, rol) FROM stdin;
    public          postgres    false    215       4780.dat            2606    16635    usuario usuario_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.usuario DROP CONSTRAINT usuario_pkey;
       public            postgres    false    215                                                                                                                                                                                4780.dat                                                                                            0000600 0004000 0002000 00000000053 14530517231 0014253 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        1	Danny	Test	Testing	danny123	23		f	0
\.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     restore.sql                                                                                         0000600 0004000 0002000 00000004377 14530517231 0015400 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        --
-- NOTE:
--
-- File paths need to be edited. Search for $$PATH$$ and
-- replace it with the path to the directory containing
-- the extracted data files.
--
--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0
-- Dumped by pg_dump version 16.0

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

DROP DATABASE users;
--
-- Name: users; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE users WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Mexico.1252';


ALTER DATABASE users OWNER TO postgres;

\connect users

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
    password character varying(50) NOT NULL,
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
\.
COPY public.usuario (id, name, lastname, username, password, age, photo, deleted, rol) FROM '$$PATH$$/4780.dat';

--
-- Name: usuario usuario_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 