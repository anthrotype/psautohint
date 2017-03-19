/* Copyright 2014 Adobe Systems Incorporated (http://www.adobe.com/). All Rights Reserved.
This software is licensed as OpenSource, under the Apache License, Version 2.0. This license is available at: http://opensource.org/licenses/Apache-2.0. */
/***********************************************************************/
#include "buildfont.h"
#include "transitionalchars.h"

/* Called when making an AFM file. */

extern void WriteCharMetrics(FILE *, indx);

extern indx create_entry(char *name,
			 char *filename,
			 int16_t width,
			 boolean derived,
			 indx dirix,
			 int16_t masters,
			 int16_t hintDir);

extern int32_t setnoncomps(void);

extern void AddCCtoTable(char *, BboxPtr, BboxPtr, int16_t, indx);

extern void AddTransitionaltoTable(char *charname, Transitions *tr);

extern void SetupCharTable(void);

/* free strings allocated for char_table */
extern void FreeCharTab(char *);

extern void sortchartab(boolean);

extern void GetWidthandBbox(char *, int16_t *, BboxPtr, boolean, indx);

/* Returns whether the given character is in the char set and has
a bez file. */
extern boolean CharExists(char *);

/* Check that a bez file has been seen for the given file name */
extern boolean CharFileExists(char *);

extern void set_char_width(char *, int32_t, int16_t *, indx);

extern int32_t writechars(boolean, char **, int32_t *, boolean, boolean);

extern int32_t writesubrs(int32_t *);

extern int32_t getCapDY(char *, boolean, indx);

extern void writefontbbox(char *);

extern void WriteBaseDesignBBox(FILE *, indx);

extern int32_t CharNameCost(void);

extern void SetCharEncoding(boolean, boolean);