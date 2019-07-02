#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <stdbool.h>

#include "getopt.h"
#include "getarg.h"
#include "gif_lib.h"

#define PROGRAM_NAME "gifremake"

#define MAX_OPERATIONS 256
#define MAX_IMAGES 2048

char command[0x80];

void Quit(status)
{
    system(command);
    exit(status);
}

bool checkbool(int value)
{
    if (value)
        return true;
    return false;
}

int getint(int *args)
{
    return *args;
}

int main(int argc, char **argv, char **envp)
{
    int ErrorCode, i;
    GifFileType *GifFileIn, *GifFileOut = (GifFileType *)NULL;
    switch (argc)
    {
    case 2:
        /* Usage: %s GifFileIn.gif  */
        /* read in a GIF */
        snprintf(command, 0x80, "rm -rf %s", argv[1]); //rm -rf GifFileIn.gif
        if ((GifFileIn = DGifOpenFileName(argv[1], &ErrorCode)) == NULL)
        {
            PrintGifError(ErrorCode);
            Quit(EXIT_FAILURE);
        }
        if (DGifSlurp(GifFileIn) == GIF_ERROR)
        {
            PrintGifError(GifFileIn->Error);
            Quit(EXIT_FAILURE);
        }
        printf("SWidth: %d\n", GifFileIn->SWidth);
        printf("SHeight: %d\n", GifFileIn->SHeight);
        printf("SColorResolution: %d\n", GifFileIn->SColorResolution);
        printf("SBackGroundColor: %d\n", GifFileIn->SBackGroundColor);
        printf("Number of Images: %d\n", GifFileIn->ImageCount);
        if (DGifCloseFile(GifFileIn, &ErrorCode) == GIF_ERROR)
        {
            PrintGifError(ErrorCode);
            Quit(EXIT_FAILURE);
        }
        break;
    case 4:
        /* Usage: %s GifFileIn.gif GifFileOut.gif argv.txt */
        snprintf(command, 0x80, "rm -rf %s %s", argv[1], argv[3]);
        int fdargs;
        fdargs = open(argv[3], O_RDONLY); //READ_ONLY
        if (fdargs == -1)
        {
            puts("ERROR: MISSING ARGUMENT!");
            Quit(EXIT_FAILURE);
        }
        char *args = malloc(0x408); //argument
        char *topargs = args + 0x400; //max argument
        memset(args, 0, 0x408);     //clean cache
        if (!read(fdargs, args, 0x400))
        { //read argument from input file
            puts("ERROR: MISSING ARGUMENT!");
            Quit(EXIT_FAILURE);
        }
        if (close(fdargs))
        {
            puts("ERROR: CANNOT CLOSE FILE!");
            Quit(EXIT_FAILURE);
        }
        /* read in a GIF */
        if ((GifFileIn = DGifOpenFileName(argv[1], &ErrorCode)) == NULL)
        {
            PrintGifError(ErrorCode);
            Quit(EXIT_FAILURE);
        }
        if (DGifSlurp(GifFileIn) == GIF_ERROR)
        {
            PrintGifError(GifFileIn->Error);
            exit(EXIT_FAILURE);
        }
        if ((GifFileOut = EGifOpenFileName(argv[2], true, &ErrorCode)) == NULL)
        {
            PrintGifError(ErrorCode);
            Quit(EXIT_FAILURE);
        }
        GifFileOut->SWidth = GifFileIn->SWidth;
        GifFileOut->SHeight = GifFileIn->SHeight;
        GifFileOut->SColorResolution = GifFileIn->SColorResolution;
        GifFileOut->SBackGroundColor = GifFileIn->SBackGroundColor;
        if (GifFileIn->SColorMap != NULL)
            GifFileOut->SColorMap = GifMakeMapObject(
                GifFileIn->SColorMap->ColorCount,
                GifFileIn->SColorMap->Colors);

        while (*args)
        {
            switch (*args++)
            {
            case 0x30: //Interlace
                for (i = 0; i < GifFileIn->ImageCount; i++) {
                    if (args >= topargs) break;
                    GifFileIn->SavedImages[i].ImageDesc.Interlace = checkbool(*args++);
                }
                break;
            case 0x40: //0x40
                for (i = 0; i < GifFileIn->ImageCount; i++)
                {
                    if (args >= topargs) break;
                    int Height = getint((int *)args);
                    args += 4;
                    int Width = getint((int *)args);
                    args += 4;
                    if (Height > 0 && GifFileIn->SavedImages[i].ImageDesc.Height < Height)
                        GifFileIn->SavedImages[i].ImageDesc.Height -= Height;
                    if (Width > 0 && GifFileIn->SavedImages[i].ImageDesc.Width < Width)
                        GifFileIn->SavedImages[i].ImageDesc.Width -= Width;
                }
                break;
            case 0x50: //Delaytime
                for (i = 0; i < GifFileIn->ImageCount; i++)
                {
                    if (args >= topargs) break;
                    GraphicsControlBlock gcb;
                    DGifSavedExtensionToGCB(GifFileIn, i, &gcb);
                    gcb.DelayTime = getint((int *)args);
                    args += 4;
                    EGifGCBToSavedExtension(&gcb, GifFileIn, i);
                }
                break;
            case 0x60: //Colormap
                for (i = 0; i < GifFileIn->ImageCount; i++)
                {
                    if (args >= topargs) break;
                    int color = getint((int *)args);
                    args += 4;
                    int BitSize = GifBitSize(color);
                    if (BitSize >= 1 && BitSize <= 8) {
                        if (GifFileIn->SavedImages[i].ImageDesc.ColorMap != NULL){
                            if (color < GifFileIn->SavedImages[i].ImageDesc.ColorMap->ColorCount)
                                GifFileIn->SavedImages[i].ImageDesc.ColorMap->ColorCount = color;
                        }
                        else GifFileIn->SavedImages[i].ImageDesc.ColorMap = GifMakeMapObject(color, NULL);
                    }
                }
                break;
            default:
                break;
            }
        }
        while (GifFileIn->ImageCount)
        {
            GifMakeSavedImage(GifFileOut, &GifFileIn->SavedImages[GifFileIn->ImageCount - 1]);
            FreeLastSavedImage(GifFileIn);
        }
        if (EGifSpew(GifFileOut) == GIF_ERROR)
            PrintGifError(GifFileOut->Error);
        else if (DGifCloseFile(GifFileIn, &ErrorCode) == GIF_ERROR)
            PrintGifError(ErrorCode);

        puts("Successfully");
        break;
    default:
        printf("Usage: %s GifFileIn.gif GifFileOut.gif argv.txt\n", argv[0]);
        exit(EXIT_FAILURE);
    }
    Quit(EXIT_SUCCESS);
}


