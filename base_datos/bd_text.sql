PGDMP                         z            test    14.4    14.4     ?           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            ?           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            ?           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            ?           1262    16394    test    DATABASE     a   CREATE DATABASE test WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Spanish_Mexico.1252';
    DROP DATABASE test;
                postgres    false            ?            1259    16395    jobs    TABLE     ?   CREATE TABLE public.jobs (
    id integer NOT NULL,
    name_job text,
    estatus text,
    start_time timestamp with time zone,
    end_time timestamp with time zone,
    job_id text
);
    DROP TABLE public.jobs;
       public         heap    postgres    false            ?            1259    16402 	   log_error    TABLE     ?   CREATE TABLE public.log_error (
    id integer NOT NULL,
    description text,
    date timestamp with time zone,
    create_date timestamp with time zone
);
    DROP TABLE public.log_error;
       public         heap    postgres    false            ?            1259    16435    log_error_id_seq    SEQUENCE     ?   ALTER TABLE public.log_error ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.log_error_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    210            ?          0    16395    jobs 
   TABLE DATA           S   COPY public.jobs (id, name_job, estatus, start_time, end_time, job_id) FROM stdin;
    public          postgres    false    209   ?       ?          0    16402 	   log_error 
   TABLE DATA           G   COPY public.log_error (id, description, date, create_date) FROM stdin;
    public          postgres    false    210          ?           0    0    log_error_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.log_error_id_seq', 1, true);
          public          postgres    false    211            a           2606    16401    jobs images_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.jobs
    ADD CONSTRAINT images_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.jobs DROP CONSTRAINT images_pkey;
       public            postgres    false    209            c           2606    16408    log_error log_error_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.log_error
    ADD CONSTRAINT log_error_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.log_error DROP CONSTRAINT log_error_pkey;
       public            postgres    false    210            ?      x?????? ? ?      ?   P   x?3?LO-Q??OR(NUH?JM.-?WH?/*JM.I?M?+I?4202?50?52P02?25?22?37??06?50?/????? ???     